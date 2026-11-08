"""
Configuration and constants for Competitive Programming README automation.
Defines repository paths, supported languages, standard rating tiers,
regular expressions, and API endpoints.
"""

from pathlib import Path
import re

# Base paths
SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
README_PATH = REPO_ROOT / "README.md"
METADATA_DIR = REPO_ROOT / "metadata"
CACHE_FILE = METADATA_DIR / "problems_cache.json"

# Codeforces API configuration
CF_API_PROBLEMS_URL = "https://codeforces.com/api/problemset.problems"
API_TIMEOUT_SECONDS = 15

# Supported programming languages and their display representations
# Matches file extensions to language definitions
SUPPORTED_LANGUAGES = {
    ".cpp": {
        "id": "cpp",
        "name": "C++",
        "table_display": "C++20",
        "metric_display": "C++ (C++17 / C++20)",
        "order": 1,
    },
    ".cc": {
        "id": "cpp",
        "name": "C++",
        "table_display": "C++20",
        "metric_display": "C++ (C++17 / C++20)",
        "order": 1,
    },
    ".cxx": {
        "id": "cpp",
        "name": "C++",
        "table_display": "C++20",
        "metric_display": "C++ (C++17 / C++20)",
        "order": 1,
    },
    ".py": {
        "id": "python",
        "name": "Python",
        "table_display": "Python 3",
        "metric_display": "Python (Python 3)",
        "order": 2,
    },
    ".java": {
        "id": "java",
        "name": "Java",
        "table_display": "Java",
        "metric_display": "Java",
        "order": 3,
    },
    ".c": {
        "id": "c",
        "name": "C",
        "table_display": "C",
        "metric_display": "C",
        "order": 4,
    },
    ".rs": {
        "id": "rust",
        "name": "Rust",
        "table_display": "Rust",
        "metric_display": "Rust",
        "order": 5,
    },
    ".go": {
        "id": "go",
        "name": "Go",
        "table_display": "Go",
        "metric_display": "Go",
        "order": 6,
    },
    ".kt": {
        "id": "kotlin",
        "name": "Kotlin",
        "table_display": "Kotlin",
        "metric_display": "Kotlin",
        "order": 7,
    },
    ".cs": {
        "id": "csharp",
        "name": "C#",
        "table_display": "C#",
        "metric_display": "C#",
        "order": 8,
    },
}

# Standard rating tier benchmarks for ICPC training roadmap
STANDARD_TIERS = [
    {
        "tier": "800",
        "numeric": 800,
        "difficulty": "Beginner",
        "focus": "Basic implementation, condition checking, array manipulation",
        "tree_comment": "Basic implementation & simulation",
    },
    {
        "tier": "900",
        "numeric": 900,
        "difficulty": "Beginner",
        "focus": "Elementary problem solving, basic math, brute-force reasoning",
        "tree_comment": "Elementary observations & brute force",
    },
    {
        "tier": "1000",
        "numeric": 1000,
        "difficulty": "Elementary",
        "focus": "Basic algorithms, greedy observations, coordinate transformations",
        "tree_comment": "Basic algorithms & greedy logic",
    },
    {
        "tier": "1100",
        "numeric": 1100,
        "difficulty": "Elementary",
        "focus": "Pattern recognition, sorting techniques, number theory basics",
        "tree_comment": "Pattern recognition (Active target)",
    },
    {
        "tier": "1200",
        "numeric": 1200,
        "difficulty": "Intermediate",
        "focus": "Algorithmic thinking, prefix sums, two pointers, binary search",
        "tree_comment": "Foundational algorithms (Active target)",
    },
    {
        "tier": "1300",
        "numeric": 1300,
        "difficulty": "Intermediate",
        "focus": "Greedy strategies, constructive algorithms, state space search",
        "tree_comment": "Greedy strategies & constructive algorithms",
    },
    {
        "tier": "1400",
        "numeric": 1400,
        "difficulty": "Intermediate",
        "focus": "Deeper problem solving, binary search on answer, elementary DP",
        "tree_comment": "Deeper problem solving & elementary DP",
    },
    {
        "tier": "1500",
        "numeric": 1500,
        "difficulty": "Advanced",
        "focus": "Combinatorics, graph traversals (BFS/DFS), modular arithmetic",
        "tree_comment": "Combinatorics & graph traversals",
    },
    {
        "tier": "1600",
        "numeric": 1600,
        "difficulty": "Advanced",
        "focus": "Stronger mathematical reasoning, trees, segment trees, game theory",
        "tree_comment": "Trees & segment trees",
    },
    {
        "tier": "1700–1900",
        "numeric": 1700,
        "difficulty": "Advanced",
        "focus": "Complex algorithms, flow networks, DP optimizations, advanced DS",
        "tree_comment": "Complex algorithms & DP optimizations",
    },
    {
        "tier": "2000+",
        "numeric": 2000,
        "difficulty": "Expert",
        "focus": "Master-level reductions, advanced graph theory, ICPC Regional sets",
        "tree_comment": "Master-level reductions & ICPC Regional sets",
    },
]

# Filename pattern: <rating>_<problem_code>.<extension>
# Examples: 800_112A.cpp, 1000_1346A.cpp, 900_208A.py
FILENAME_PATTERN = re.compile(r"^(\d+)_([A-Za-z0-9_]+)\.([A-Za-z0-9]+)$")

# Codeforces code pattern: e.g. 112A, 1346A, 1520F1
CF_CODE_PATTERN = re.compile(r"^(\d+)([A-Za-z][0-9]?|[A-Za-z]+)$")

