#!/usr/bin/env python3
"""
Automated README Synchronization Workflow for Competitive Programming.
Scans solution files across rating directories, calculates repository metrics,
fetches official problem titles via Codeforces API / local cache, and safely
synchronizes README.md dynamic sections.
"""

import argparse
from dataclasses import dataclass, field
import difflib
import logging
from pathlib import Path
import re
import sys
from typing import Dict, List, Optional, Set, Tuple

# Add scripts directory to path to support running from any directory
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from codeforces_api import CodeforcesAPI
from config import (
    CACHE_FILE,
    CF_CODE_PATTERN,
    FILENAME_PATTERN,
    README_PATH,
    REPO_ROOT,
    STANDARD_TIERS,
    SUPPORTED_LANGUAGES,
)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("update_readme")


@dataclass
class SolutionFile:
    """Represents an individual source solution file on disk."""
    path: Path
    rel_path: Path
    filename: str
    rating: int
    problem_code: str
    extension: str
    lang_id: str
    lang_name: str
    lang_table: str
    lang_metric: str
    lang_order: int


@dataclass
class Problem:
    """Represents a unique algorithmic problem with one or more implementations."""
    rating: int
    problem_code: str
    contest_id: Optional[int]
    index: Optional[str]
    title: str = "Unknown"
    url: Optional[str] = None
    is_codeforces: bool = True
    files: List[SolutionFile] = field(default_factory=list)

    @property
    def languages_table(self) -> str:
        """Returns slash-separated language names for the markdown archive table."""
        unique_langs = []
        for f in sorted(self.files, key=lambda x: (x.lang_order, x.extension)):
            if f.lang_table not in unique_langs:
                unique_langs.append(f.lang_table)
        return " / ".join(unique_langs)

    @property
    def solution_links_table(self) -> str:
        """Returns markdown solution links joined by ' | ' for table column."""
        links = []
        for f in sorted(self.files, key=lambda x: (x.lang_order, x.extension)):
            links.append(f"[`{f.filename}`](./{f.rating}/{f.filename})")
        return " \\| ".join(links)

    @property
    def platform_link_table(self) -> str:
        """Returns the platform markdown link."""
        if self.is_codeforces and self.url:
            return f"[Codeforces {self.problem_code}]({self.url})"
        return "-"


class RepositoryScanner:
    """Scans and validates solution files in the repository."""

    def __init__(self, root: Path = REPO_ROOT):
        self.root = root
        self.solution_files: List[SolutionFile] = []
        self.problems_map: Dict[Tuple[int, str], Problem] = {}
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def scan(self) -> None:
        """Discovers rating directories and parses solution files."""
        self.solution_files.clear()
        self.problems_map.clear()
        self.errors.clear()
        self.warnings.clear()

        # Find all rating directories (e.g. 800, 900, 1000)
        rating_dirs = [d for d in self.root.iterdir() if d.is_dir() and d.name.isdigit()]
        rating_dirs.sort(key=lambda d: int(d.name))

        for r_dir in rating_dirs:
            dir_rating = int(r_dir.name)
            for item in r_dir.iterdir():
                if not item.is_file():
                    continue

                filename = item.name
                match = FILENAME_PATTERN.match(filename)
                if not match:
                    # Ignore compiled binaries or hidden artifacts
                    if item.suffix.lower() not in [".exe", ".out", ".o", ".obj", ".gitkeep"]:
                        self.warnings.append(
                            f"File '{item.relative_to(self.root)}' does not follow <rating>_<problem_code>.<ext> convention."
                        )
                    continue

                file_rating = int(match.group(1))
                problem_code = match.group(2)
                ext = f".{match.group(3).lower()}"

                if file_rating != dir_rating:
                    self.warnings.append(
                        f"Rating mismatch: File '{filename}' has prefix '{file_rating}' but resides in '{dir_rating}/'."
                    )

                # Silently ignore compiled binary and object files
                if ext in [".exe", ".o", ".obj", ".out", ".class", ".pdb", ".ilk", ".idb", ".dylib", ".so", ".dll"]:
                    continue

                if ext not in SUPPORTED_LANGUAGES:
                    self.warnings.append(f"Unrecognized language extension '{ext}' in file '{filename}'.")
                    continue

                lang_info = SUPPORTED_LANGUAGES[ext]
                sol_file = SolutionFile(
                    path=item,
                    rel_path=item.relative_to(self.root),
                    filename=filename,
                    rating=dir_rating,
                    problem_code=problem_code,
                    extension=ext,
                    lang_id=lang_info["id"],
                    lang_name=lang_info["name"],
                    lang_table=lang_info["table_display"],
                    lang_metric=lang_info["metric_display"],
                    lang_order=lang_info["order"],
                )
                self.solution_files.append(sol_file)

                # Group into Problem instance
                key = (dir_rating, problem_code)
                if key not in self.problems_map:
                    cid, idx = CodeforcesAPI.parse_problem_code(problem_code)
                    self.problems_map[key] = Problem(
                        rating=dir_rating,
                        problem_code=problem_code,
                        contest_id=cid,
                        index=idx,
                        is_codeforces=(cid is not None and idx is not None),
                    )
                self.problems_map[key].files.append(sol_file)

    def get_sorted_problems(self) -> List[Problem]:
        """
        Sorts problems by rating ascending, then by contestId (numeric) and index.
        """
        def sort_key(p: Problem):
            cid_sort = p.contest_id if p.contest_id is not None else 999999
            idx_sort = p.index if p.index is not None else p.problem_code
            return (p.rating, cid_sort, idx_sort)

        return sorted(self.problems_map.values(), key=sort_key)


class ReadmeGenerator:
    """Generates formatted Markdown content for dynamic sections."""

    def __init__(self, scanner: RepositoryScanner, api: CodeforcesAPI):
        self.scanner = scanner
        self.api = api

    def generate_directory_structure_content(self) -> str:
        """
        Generates the directory tree block matching existing alignment and hierarchy.
        """
        lines = [
            "```text",
            "Competitive-Programming/",
        ]

        def add_tree_line(prefix_text: str, comment: str) -> None:
            padding = max(1, 42 - len(prefix_text))
            lines.append(f"{prefix_text}{' ' * padding}# {comment}")

        # Check .github workflows
        workflow_file = REPO_ROOT / ".github" / "workflows" / "update-readme.yml"
        if workflow_file.exists():
            add_tree_line("├── .github/workflows/", "GitHub Actions CI/CD automation")
            add_tree_line("│   └── update-readme.yml", "Immediate push-triggered README sync")

        # Map problems by rating
        rating_groups: Dict[int, List[Problem]] = {}
        for p in self.scanner.get_sorted_problems():
            rating_groups.setdefault(p.rating, []).append(p)

        # Standard tiers comments and active targets
        tier_info_map = {t["numeric"]: t for t in STANDARD_TIERS if "numeric" in t}
        all_numeric_ratings = sorted(set(list(rating_groups.keys()) + [t["numeric"] for t in STANDARD_TIERS if "numeric" in t]))

        # Include rating tiers up to max active or standard range
        max_solved_rating = max(rating_groups.keys()) if rating_groups else 800
        target_shown = 0

        for r in all_numeric_ratings:
            t_info = tier_info_map.get(r, {
                "tier": str(r),
                "difficulty": "Unknown",
                "focus": "Algorithmic problems",
                "tree_comment": f"Rating {r}",
            })
            probs = rating_groups.get(r, [])

            if probs:
                tree_comment = t_info.get("tree_comment", f"Rating {r}: Algorithmic development")
                if not tree_comment.startswith("Rating "):
                    tree_comment = f"Rating {r}: {tree_comment}"
                
                # Format directory line with padding to column 43
                dir_line = f"├── {r}/"
                add_tree_line(dir_line, tree_comment)

                # List files in rating folder
                files_in_rating = []
                for p in probs:
                    for f in sorted(p.files, key=lambda x: (x.lang_order, x.filename)):
                        files_in_rating.append(f.filename)

                if len(files_in_rating) <= 4:
                    for idx, fname in enumerate(files_in_rating):
                        prefix = "└── " if idx == len(files_in_rating) - 1 else "├── "
                        lines.append(f"│   {prefix}{fname}")
                else:
                    for fname in files_in_rating[:4]:
                        lines.append(f"│   ├── {fname}")
                    lines.append("│   └── ...")

            else:
                # Show up to 2 empty target tiers following the max solved rating
                if r > max_solved_rating and target_shown < 2:
                    target_shown += 1
                    t_comment = t_info.get("tree_comment", "Active target")
                    if "Active target" not in t_comment:
                        t_comment = f"{t_comment} (Active target)"
                    if not t_comment.startswith(f"Rating {r}:"):
                        t_comment = f"Rating {r}: {t_comment}"
                    
                    dir_line = f"├── {r}/"
                    add_tree_line(dir_line, t_comment)

        # Summary branch and companion files
        add_tree_line("├── ...", "Scalable hierarchy up to 2000+")
        
        # Check metadata directory
        meta_dir = REPO_ROOT / "metadata"
        if meta_dir.exists():
            add_tree_line("├── metadata/", "Local problem metadata & API cache")
            cache_file = meta_dir / "problems_cache.json"
            if cache_file.exists():
                add_tree_line("│   └── problems_cache.json", "Offline problem definitions & tags")

        # Check scripts directory
        scripts_dir = REPO_ROOT / "scripts"
        if scripts_dir.exists():
            add_tree_line("├── scripts/", "Repository automation & README sync engine")
            script_files = sorted([f.name for f in scripts_dir.glob("*.py")])
            for idx, sname in enumerate(script_files):
                prefix = "└── " if idx == len(script_files) - 1 else "├── "
                script_comments = {
                    "codeforces_api.py": "Codeforces API client & cache resolver",
                    "config.py": "Configurations & language definitions",
                    "install_hooks.py": "Local Git pre-push hook manager",
                    "update_readme.py": "Main synchronization script",
                }
                s_desc = script_comments.get(sname, "Automation script")
                add_tree_line(f"│   {prefix}{sname}", s_desc)

        if (REPO_ROOT / "COMPETITIVE_PROGRAMMING_ROADMAP.md").exists():
            add_tree_line("├── COMPETITIVE_PROGRAMMING_ROADMAP.md", "In-depth 14-chapter curriculum & theoretical syllabus")

        if (REPO_ROOT / "README_AUTOMATION.md").exists():
            add_tree_line("├── README_AUTOMATION.md", "Comprehensive automation guide & workflows")

        if (REPO_ROOT / "requirements.txt").exists():
            add_tree_line("├── requirements.txt", "Python dependencies (requests)")

        if (REPO_ROOT / ".gitignore").exists():
            add_tree_line("├── .gitignore", "Standard build & binary exclusion rules")

        if (REPO_ROOT / "README.md").exists():
            add_tree_line("└── README.md", "Repository documentation")

        lines.append("```")
        return "\n".join(lines)

    def generate_rating_progression_table(self) -> str:
        """Generates the Rating Progression & Problem Collection table."""
        lines = [
            "| Rating Tier | Difficulty Level | Primary Cognitive Focus | Status |",
            "| :---: | :---: | :--- | :---: |",
        ]

        rating_groups: Dict[int, List[Problem]] = {}
        for p in self.scanner.get_sorted_problems():
            rating_groups.setdefault(p.rating, []).append(p)

        max_solved = max(rating_groups.keys()) if rating_groups else 0
        in_progress_marked = False

        for tier in STANDARD_TIERS:
            numeric = tier.get("numeric", 0)
            probs = rating_groups.get(numeric, [])
            total_files = sum(len(p.files) for p in probs)
            unique_count = len(probs)

            if unique_count > 0:
                if unique_count == total_files:
                    status = f"[{unique_count} Solved](./{tier['tier']}/)"
                else:
                    status = f"[{unique_count} Solved ({total_files} files)](./{tier['tier']}/)"
            else:
                if numeric > max_solved and not in_progress_marked:
                    status = "*In Progress*"
                    in_progress_marked = True
                else:
                    status = "*Target*"

            lines.append(
                f"| **{tier['tier']}** | {tier['difficulty']} | {tier['focus']} | {status} |"
            )

        return "\n".join(lines)

    def generate_repository_metrics(self) -> str:
        """Generates the Current Repository Metrics bullet list."""
        total_files = len(self.scanner.solution_files)
        problems = self.scanner.get_sorted_problems()
        total_unique = len(problems)

        # Language distribution
        lang_counts: Dict[str, int] = {}
        for f in self.scanner.solution_files:
            lang_counts[f.lang_metric] = lang_counts.get(f.lang_metric, 0) + 1

        # Rating distribution
        rating_groups: Dict[int, List[Problem]] = {}
        for p in problems:
            rating_groups.setdefault(p.rating, []).append(p)

        lines = [
            "*Statistics verified directly from current workspace source files:*",
            "",
            f"- **Total Solutions Stored**: {total_files} files",
            f"- **Unique Problems Solved**: {total_unique}",
            "- **Language Distribution**:",
        ]

        # Sort languages consistently by order defined in config
        ordered_metric_names = []
        for lang in sorted(SUPPORTED_LANGUAGES.values(), key=lambda x: x["order"]):
            m = lang["metric_display"]
            if m not in ordered_metric_names:
                ordered_metric_names.append(m)

        for m in ordered_metric_names:
            if m in lang_counts:
                count = lang_counts[m]
                word = "solution" if count == 1 else "solutions"
                lines.append(f"  - **{m}**: {count} {word}")

        lines.append("- **Rating Distribution**:")
        for r in sorted(rating_groups.keys()):
            r_probs = rating_groups[r]
            r_files = sum(len(p.files) for p in r_probs)
            r_unique = len(r_probs)

            if r_unique == r_files:
                word = "solution" if r_files == 1 else "solutions"
                lines.append(f"  - **{r}**: {r_files} {word}")
            else:
                # Multi-file or multi-language breakdown
                r_lang_counts: Dict[str, int] = {}
                for p in r_probs:
                    for f in p.files:
                        r_lang_counts[f.lang_name] = r_lang_counts.get(f.lang_name, 0) + 1

                lang_parts = [f"{count} {lang}" for lang, count in r_lang_counts.items()]
                lang_str = ", ".join(lang_parts)

                multi_problems = [p.problem_code for p in r_probs if len(p.files) > 1]
                if len(multi_problems) == 1:
                    multi_str = f"*{multi_problems[0]} implemented in both languages*"
                else:
                    multi_str = f"*{', '.join(multi_problems)} implemented in multiple languages*"

                lines.append(
                    f"  - **{r}**: {r_unique} unique problems ({lang_str} — {multi_str})"
                )

        return "\n".join(lines)

    def generate_solution_archive(self) -> str:
        """Generates the Verified Solution Archive collapsible markdown table."""
        problems = self.scanner.get_sorted_problems()
        total_unique = len(problems)

        lines = [
            "<details open>",
            f"<summary><b>Click to expand / collapse full problem index ({total_unique} problems)</b></summary>",
            "",
            "<br/>",
            "",
            "| Rating | Code | Problem Title | Solution | Language | Platform Link |",
            "| :---: | :---: | :--- | :---: | :---: | :---: |",
        ]

        for p in problems:
            # Codeforces API metadata lookup
            meta = self.api.resolve_problem(
                problem_code=p.problem_code,
                expected_rating=p.rating,
                readme_fallback_title=p.title if p.title != "Unknown" else None,
            )
            p.title = meta.get("name", "Unknown").replace("|", "\\|")
            p.url = meta.get("url")
            p.is_codeforces = meta.get("is_codeforces", True)

            lines.append(
                f"| `{p.rating}` | **{p.problem_code}** | {p.title} | {p.solution_links_table} | {p.languages_table} | {p.platform_link_table} |"
            )

        lines.append("")
        lines.append("</details>")
        return "\n".join(lines)


class ReadmeSynchronizer:
    """Manages parsing existing README, replacing dynamic sections, and validating safety."""

    # Section comment markers for guaranteed safe delimitation
    MARKERS = {
        "DIR_TREE": ("<!-- AUTO-GEN:DIRECTORY_STRUCTURE:START -->", "<!-- AUTO-GEN:DIRECTORY_STRUCTURE:END -->"),
        "RATING_TABLE": ("<!-- AUTO-GEN:RATING_TABLE:START -->", "<!-- AUTO-GEN:RATING_TABLE:END -->"),
        "METRICS": ("<!-- AUTO-GEN:METRICS:START -->", "<!-- AUTO-GEN:METRICS:END -->"),
        "ARCHIVE": ("<!-- AUTO-GEN:ARCHIVE:START -->", "<!-- AUTO-GEN:ARCHIVE:END -->"),
    }

    def __init__(self, readme_path: Path = README_PATH):
        self.readme_path = readme_path
        self.original_content = ""
        self.load_readme()

    def load_readme(self) -> None:
        """Reads current README.md content with UTF-8 encoding."""
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README file not found at {self.readme_path}")
        with open(self.readme_path, "r", encoding="utf-8") as f:
            self.original_content = f.read()

    def parse_existing_titles_from_archive(self) -> Dict[str, str]:
        """Extracts existing verified problem titles from README table as safe fallbacks."""
        titles: Dict[str, str] = {}
        pattern = re.compile(
            r"^\|\s*`\d+`\s*\|\s*\*\*([A-Za-z0-9_]+)\*\*\s*\|\s*([^|]+?)\s*\|",
            re.MULTILINE,
        )
        for match in pattern.finditer(self.original_content):
            code = match.group(1).strip()
            title = match.group(2).strip()
            if title and title not in ("Unknown", "Not retrieved"):
                titles[code] = title
        return titles

    def parse_existing_stats(self) -> Dict[str, int]:
        """Extracts existing numeric statistics from README."""
        stats = {}
        m_files = re.search(r"-\s*\*\*Total Solutions Stored\*\*:\s*(\d+)\s*files", self.original_content)
        m_unique = re.search(r"-\s*\*\*Unique Problems Solved\*\*:\s*(\d+)", self.original_content)
        m_cpp = re.search(r"-\s*\*\*C\+\+.*?\*\*:\s*(\d+)\s*solution", self.original_content)
        m_py = re.search(r"-\s*\*\*Python.*?\*\*:\s*(\d+)\s*solution", self.original_content)

        if m_files:
            stats["total_files"] = int(m_files.group(1))
        if m_unique:
            stats["unique_problems"] = int(m_unique.group(1))
        if m_cpp:
            stats["cpp_solutions"] = int(m_cpp.group(1))
        if m_py:
            stats["python_solutions"] = int(m_py.group(1))

        # Also extract problem codes currently present in the archive
        codes = re.findall(r"^\|\s*`\d+`\s*\|\s*\*\*([A-Za-z0-9_]+)\*\*", self.original_content, re.MULTILINE)
        stats["problem_codes"] = set(codes)
        return stats

    def replace_section(
        self,
        content: str,
        section_key: str,
        new_content: str,
        fallback_regex: str,
    ) -> str:
        """
        Replaces a section using either AUTO-GEN comment markers or regex boundaries.
        Always preserves surrounding static Markdown.
        """
        start_marker, end_marker = self.MARKERS[section_key]

        # Check if markers already exist
        if start_marker in content and end_marker in content:
            pattern = re.compile(
                re.escape(start_marker) + r".*?" + re.escape(end_marker),
                re.DOTALL,
            )
            replacement = f"{start_marker}\n{new_content}\n{end_marker}"
            return pattern.sub(replacement, content, count=1)

        # Fallback to regex pattern matching for initial conversion
        pattern = re.compile(fallback_regex, re.DOTALL | re.MULTILINE)
        match = pattern.search(content)
        if match:
            replacement = f"{start_marker}\n{new_content}\n{end_marker}"
            return content[:match.start()] + replacement + content[match.end():]

        logger.warning("Could not locate boundaries for dynamic section '%s'.", section_key)
        return content

    def synchronize(self, generator: ReadmeGenerator) -> Tuple[str, bool, List[str]]:
        """
        Synchronizes all 4 dynamic sections:
        1. Directory Structure tree
        2. Rating Progression table
        3. Repository Metrics
        4. Verified Solution Archive
        Returns (new_content, has_changed, modified_sections).
        """
        content = self.original_content
        modified_sections = []

        # 1. Directory Structure
        new_tree = generator.generate_directory_structure_content()
        tree_regex = r"```text\s*\nCompetitive-Programming/.*?```"
        tree_replaced = self.replace_section(content, "DIR_TREE", new_tree, tree_regex)
        if tree_replaced != content:
            modified_sections.append("Directory Structure")
            content = tree_replaced

        # 2. Rating Progression Table
        new_table = generator.generate_rating_progression_table()
        table_regex = r"(\| Rating Tier \| Difficulty Level \|.*?\|\s*\n)(?=\s*\n### Current Repository Metrics)"
        table_replaced = self.replace_section(content, "RATING_TABLE", new_table, table_regex)
        if table_replaced != content:
            modified_sections.append("Rating Progression & Problem Collection")
            content = table_replaced

        # 3. Repository Metrics
        new_metrics = generator.generate_repository_metrics()
        metrics_regex = r"(\*Statistics verified directly from current workspace source files:\*.*?\n\s*- \*\*Rating Distribution\*\*:.*?\n(?:  - \*\*.*?\n)+)(?=\s*\n### Verified Solution Archive)"
        metrics_replaced = self.replace_section(content, "METRICS", new_metrics, metrics_regex)
        if metrics_replaced != content:
            modified_sections.append("Repository Metrics")
            content = metrics_replaced

        # 4. Verified Solution Archive
        new_archive = generator.generate_solution_archive()
        archive_regex = r"(<details open>\s*\n<summary><b>Click to expand / collapse full problem index.*?<\/details>)"
        archive_replaced = self.replace_section(content, "ARCHIVE", new_archive, archive_regex)
        if archive_replaced != content:
            modified_sections.append("Verified Solution Archive")
            content = archive_replaced

        has_changed = (content != self.original_content)
        return content, has_changed, modified_sections


def validate_repository_and_links(scanner: RepositoryScanner, updated_content: str) -> List[str]:
    """
    Validates repository consistency:
    - Verifies that all generated markdown solution links correspond to existing disk files.
    - Verifies count consistency.
    """
    errors = []
    total_files = len(scanner.solution_files)
    problems = scanner.get_sorted_problems()

    # Link validation
    link_pattern = re.compile(r"\[`([^`]+)`\]\(\.\/(\d+)\/([^)]+)\)")
    for match in link_pattern.finditer(updated_content):
        displayed_name = match.group(1)
        folder = match.group(2)
        target_path = REPO_ROOT / folder / displayed_name
        if not target_path.exists():
            errors.append(f"Broken link in README: file does not exist at {target_path}")

    # Consistency check
    sum_files = sum(len(p.files) for p in problems)
    if sum_files != total_files:
        errors.append(f"Inconsistent file count: scanner has {total_files}, problem instances total {sum_files}")

    return errors


def print_summary(
    old_stats: Dict[str, int],
    scanner: RepositoryScanner,
    modified_sections: List[str],
    has_changed: bool,
) -> None:
    """Prints a clear, executive summary of detected changes."""
    print("========================================")
    print("       README SYNCHRONIZATION")
    print("========================================")

    if not has_changed:
        print("README is already synchronized with the repository.")
        print("No changes needed.")
        print("========================================")
        return

    total_files = len(scanner.solution_files)
    unique_problems = len(scanner.problems_map)

    # Count by language
    cpp_count = sum(1 for f in scanner.solution_files if f.lang_id == "cpp")
    py_count = sum(1 for f in scanner.solution_files if f.lang_id == "python")

    old_total = old_stats.get("total_files", total_files)
    old_unique = old_stats.get("unique_problems", unique_problems)
    old_cpp = old_stats.get("cpp_solutions", cpp_count)
    old_py = old_stats.get("python_solutions", py_count)

    print(f"Total source files:       {old_total:>2} -> {total_files}")
    print(f"Unique problems:          {old_unique:>2} -> {unique_problems}")
    print(f"C++ solutions:            {old_cpp:>2} -> {cpp_count}")
    print(f"Python solutions:         {old_py:>2} -> {py_count}")

    # New or removed problems
    current_codes = {p.problem_code for p in scanner.problems_map.values()}
    old_codes = old_stats.get("problem_codes", set())

    new_codes = sorted(current_codes - old_codes)
    removed_codes = sorted(old_codes - current_codes)

    if new_codes:
        print("\nNew problems detected:")
        for c in new_codes:
            for p in scanner.problems_map.values():
                if p.problem_code == c:
                    for f in p.files:
                        print(f"  + {f.filename}")

    if removed_codes:
        print("\nRemoved problems:")
        for c in removed_codes:
            print(f"  - Problem {c}")

    if modified_sections:
        print("\nModified sections:")
        for sec in modified_sections:
            print(f"  - {sec}")

    print("\nREADME successfully synchronized.")
    print("Please review the changes before committing.")
    print("========================================")


def main():
    parser = argparse.ArgumentParser(
        description="Synchronize README.md with actual competitive programming solutions on disk."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if README is synchronized without modifying files. Returns exit code 1 if out of sync.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate execution and print changes without modifying README.md.",
    )
    parser.add_argument(
        "--refresh-cache",
        action="store_true",
        help="Force re-fetching problem metadata from the Codeforces API.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress informational output.",
    )
    args = parser.parse_args()

    # Step 1: Scan repository
    scanner = RepositoryScanner(REPO_ROOT)
    scanner.scan()

    if scanner.warnings and not args.quiet:
        for w in scanner.warnings:
            logger.warning(w)

    # Step 2: Initialize API and synchronizer
    api = CodeforcesAPI(CACHE_FILE)
    if args.refresh_cache:
        api.fetch_api_problemset()

    synchronizer = ReadmeSynchronizer(README_PATH)
    old_stats = synchronizer.parse_existing_stats()

    # Seed fallback titles from existing README for problems not yet cached
    readme_titles = synchronizer.parse_existing_titles_from_archive()
    for (rating, code), prob in scanner.problems_map.items():
        if code in readme_titles:
            prob.title = readme_titles[code]

    # Step 3: Generate synchronized content
    generator = ReadmeGenerator(scanner, api)
    updated_content, has_changed, modified_sections = synchronizer.synchronize(generator)

    # Save any newly resolved metadata to cache
    api.save_cache()

    # Step 4: Validate generated content
    validation_errors = validate_repository_and_links(scanner, updated_content)
    if validation_errors:
        logger.error("Validation failed with %d errors:", len(validation_errors))
        for err in validation_errors:
            logger.error("  - %s", err)
        sys.exit(1)

    # Step 5: Handle check mode
    if args.check:
        if has_changed:
            if not args.quiet:
                print("README.md is out of sync with repository source files.")
            sys.exit(1)
        else:
            if not args.quiet:
                print("README.md is synchronized.")
            sys.exit(0)

    # Step 6: Handle dry-run or write
    if not args.quiet:
        print_summary(old_stats, scanner, modified_sections, has_changed)

    if has_changed and not args.dry_run:
        # Atomic file write with UTF-8
        temp_readme = README_PATH.with_suffix(".tmp")
        try:
            with open(temp_readme, "w", encoding="utf-8") as f:
                f.write(updated_content)
            temp_readme.replace(README_PATH)
        except Exception as e:
            logger.error("Failed to write updated README.md: %s", e)
            if temp_readme.exists():
                temp_readme.unlink()
            sys.exit(1)


if __name__ == "__main__":
    main()

