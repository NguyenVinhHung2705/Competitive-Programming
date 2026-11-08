#!/usr/bin/env python3
"""
Git Hook Installer for Competitive Programming Repository Automation.
Installs a safe, loop-free pre-push hook that ensures README.md is always
synchronized with source code solutions before pushing to remote.
"""

import argparse
from pathlib import Path
import stat
import sys

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
GIT_HOOKS_DIR = REPO_ROOT / ".git" / "hooks"
PRE_PUSH_HOOK = GIT_HOOKS_DIR / "pre-push"
PRE_COMMIT_HOOK = GIT_HOOKS_DIR / "pre-commit"

PRE_PUSH_SCRIPT = """#!/bin/sh
# Anti-loop pre-push hook for Competitive Programming README synchronization
# Ensures README.md accurately reflects repository solutions before pushing to GitHub.

echo "=========================================================="
echo " [PRE-PUSH] Checking README.md synchronization..."
echo "=========================================================="

# Check if Python is available
if command -v python >/dev/null 2>&1; then
    PY_CMD="python"
elif command -v python3 >/dev/null 2>&1; then
    PY_CMD="python3"
elif command -v py >/dev/null 2>&1; then
    PY_CMD="py"
else
    echo "[PRE-PUSH WARNING] Python not found in PATH. Skipping README check."
    exit 0
fi

# Run the synchronization check
$PY_CMD scripts/update_readme.py --check --quiet
CHECK_STATUS=$?

if [ $CHECK_STATUS -ne 0 ]; then
    echo ""
    echo "[PRE-PUSH] README.md is out of sync with solution files."
    echo "[PRE-PUSH] Synchronizing README.md now..."
    echo ""
    $PY_CMD scripts/update_readme.py

    echo ""
    echo "=========================================================="
    echo " [PRE-PUSH NOTIFICATION] PUSH PAUSED FOR REVIEW"
    echo "=========================================================="
    echo " README.md has been automatically synchronized."
    echo " Please review and commit the changes before pushing:"
    echo ""
    echo "   1. Review changes:  git diff README.md"
    echo "   2. Stage files:     git add README.md metadata/"
    echo "   3. Commit updates:  git commit -m \\"docs: automatically update README after new solutions\\""
    echo "   4. Push to GitHub:  git push"
    echo "=========================================================="
    echo ""
    exit 1
fi

echo "[PRE-PUSH] README.md is verified and fully synchronized."
exit 0
"""

PRE_COMMIT_SCRIPT = """#!/bin/sh
# Pre-commit hook to verify README synchronization
if command -v python >/dev/null 2>&1; then
    PY_CMD="python"
elif command -v python3 >/dev/null 2>&1; then
    PY_CMD="python3"
elif command -v py >/dev/null 2>&1; then
    PY_CMD="py"
else
    exit 0
fi

$PY_CMD scripts/update_readme.py --check --quiet
if [ $? -ne 0 ]; then
    echo "[PRE-COMMIT] Notice: Solution files have changed. Running README sync..."
    $PY_CMD scripts/update_readme.py
    echo "[PRE-COMMIT] README.md updated. Please run 'git add README.md' before completing commit."
    exit 1
fi
exit 0
"""


def install_hook(hook_type: str = "pre-push") -> bool:
    """Installs the designated Git hook."""
    if not (REPO_ROOT / ".git").exists():
        print(f"Error: {REPO_ROOT} is not a git repository.")
        return False

    GIT_HOOKS_DIR.mkdir(parents=True, exist_ok=True)

    if hook_type == "pre-push":
        target = PRE_PUSH_HOOK
        content = PRE_PUSH_SCRIPT
    elif hook_type == "pre-commit":
        target = PRE_COMMIT_HOOK
        content = PRE_COMMIT_SCRIPT
    else:
        print(f"Unknown hook type: {hook_type}")
        return False

    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    # Make executable on Unix / Git Bash environments
    try:
        current_stat = target.stat().st_mode
        target.chmod(current_stat | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except Exception:
        pass

    print(f"Successfully installed Git {hook_type} hook at:")
    print(f"  {target}")
    return True


def uninstall_hook(hook_type: str = "pre-push") -> bool:
    """Removes the designated Git hook."""
    target = PRE_PUSH_HOOK if hook_type == "pre-push" else PRE_COMMIT_HOOK
    if target.exists():
        target.unlink()
        print(f"Successfully removed Git {hook_type} hook.")
        return True
    else:
        print(f"Git {hook_type} hook is not currently installed.")
        return False


def main():
    parser = argparse.ArgumentParser(description="Install or manage Git hooks for README synchronization.")
    parser.add_argument(
        "--hook",
        choices=["pre-push", "pre-commit"],
        default="pre-push",
        help="Type of Git hook to configure (default: pre-push).",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="Uninstall the specified hook.",
    )
    args = parser.parse_args()

    if args.uninstall:
        uninstall_hook(args.hook)
    else:
        install_hook(args.hook)


if __name__ == "__main__":
    main()

