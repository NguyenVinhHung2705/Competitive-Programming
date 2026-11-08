# Automated README Synchronization System (Immediate Git Push & Cloud Workflow)

This document provides a comprehensive guide to the **Competitive Programming README Automation System** designed for continuous preparation toward **ICPC 2027**.

The automation operates in two modes:
1. **Immediate Cloud Automation (GitHub Actions)**: Automatically synchronizes `README.md` immediately whenever new solution files are pushed to GitHub — running on GitHub-hosted runners even when your local machine is shut down, sleeping, or offline.
2. **Local CLI Execution**: On-demand and Git-hook-driven execution for offline development and local validation.

---

## 1. Immediate Cloud Automation Architecture (GitHub Actions)

The cloud workflow runs on GitHub-hosted Ubuntu runners immediately upon pushing new solution files:

```
               [git push to main with solution files in [0-9]*/**]
                                       OR
                       [Manual trigger: workflow_dispatch]
                                       |
                                       v
                     +-----------------------------------+
                     |  GitHub Actions (ubuntu-latest)   |
                     |  .github/workflows/               |
                     |  update-readme.yml                |
                     +-----------------+-----------------+
                                       |
              +------------------------+------------------------+
              |                                                 |
              v                                                 v
      +-------------------------------+             +-------------------------------+
      | 1. Checkout Repository        |             | 2. Setup Python 3.12          |
      |    (actions/checkout@v4)      |             |    & Install Dependencies     |
      +---------------+---------------+             +---------------+---------------+
                      |                                             |
                      +----------------------+----------------------+
                                             |
                                             v
                              +-------------------------------+
                              | 3. Execute Updater            |
                              |    python scripts/            |
                              |    update_readme.py           |
                              +--------------+----------------+
                                             |
                                             v
                              +-------------------------------+
                              | 4. Validate Generated Content |
                              |    python scripts/            |
                              |    update_readme.py --check   |
                              +--------------+----------------+
                                             |
                         +-------------------+-------------------+
                         |                                       |
                         | (No changes)                          | (Changes detected)
                         v                                       v
          +-----------------------------+         +-------------------------------+
          | No commit created           |         | Pull latest remote branch:    |
          | Exit 0 (Clean finish)       |         | git pull --rebase origin main |
          +-----------------------------+         +---------------+---------------+
                                                                  |
                                                                  v
                                                  +-------------------------------+
                                                  | Configure bot identity:       |
                                                  | github-actions[bot]           |
                                                  +---------------+---------------+
                                                                  |
                                                                  v
                                                  +-------------------------------+
                                                  | Stage README.md only:         |
                                                  | git add README.md             |
                                                  | git commit -m "docs: auto..." |
                                                  +---------------+---------------+
                                                                  |
                                                                  v
                                                  +-------------------------------+
                                                  | Push to default branch (main) |
                                                  | (GITHUB_TOKEN permissions)    |
                                                  +-------------------------------+
```

---

## 2. GitHub Actions Workflow Configuration

The workflow file is located at:
```text
.github/workflows/update-readme.yml
```

### 1. Push Trigger & Precision Path Filtering

The workflow triggers immediately when changes are pushed to `main`, but **strictly targets solution files** located inside rating directories:

```yaml
'on':
  push:
    branches:
      - main
    paths:
      - '[0-9]*/*.cpp'
      - '[0-9]*/*.cc'
      - '[0-9]*/*.cxx'
      - '[0-9]*/*.py'
      - '[0-9]*/*.c'
      - '[0-9]*/*.java'
      - '[0-9]*/*.rs'
      - '[0-9]*/*.go'
      - '[0-9]*/*.kt'
      - '[0-9]*/*.cs'
      - '[0-9]*/**/*.cpp'
      - '[0-9]*/**/*.cc'
      - '[0-9]*/**/*.cxx'
      - '[0-9]*/**/*.py'
      - '[0-9]*/**/*.c'
      - '[0-9]*/**/*.java'
      - '[0-9]*/**/*.rs'
      - '[0-9]*/**/*.go'
      - '[0-9]*/**/*.kt'
      - '[0-9]*/**/*.cs'
  workflow_dispatch:
```

### 2. Path Filter Isolation Guarantees

| File Changed on Push | Triggers Workflow? | Reason |
|---|---|---|
| `800/800_112A.cpp` | **YES** | Matches `[0-9]*/*.cpp` |
| `900/900_208A.py` | **YES** | Matches `[0-9]*/*.py` |
| `1000/1000_90A.cpp` | **YES** | Matches `[0-9]*/*.cpp` |
| `1100/1100_123A.cpp` | **YES** | Matches `[0-9]*/*.cpp` (new rating tier) |
| `README.md` | **NO** | Excluded; does not match rating directory pattern |
| `README_AUTOMATION.md` | **NO** | Excluded; documentation change |
| `scripts/update_readme.py` | **NO** | Excluded; `scripts/` does not start with `[0-9]` |
| `scripts/codeforces_api.py`| **NO** | Excluded; automation script change |
| `.github/workflows/*.yml` | **NO** | Excluded; workflow definition change |
| `metadata/problems_cache.json` | **NO** | Excluded; cache change |
| `requirements.txt` | **NO** | Excluded; root dependency change |

### 3. Concurrency & Infinite Loop Prevention

1. **Path-Filtered Push**: Commits generated by the bot touch `README.md` only. Since `README.md` does not match the `paths` filter, the bot's commit will **never** trigger a new workflow run.
2. **Native `GITHUB_TOKEN` Isolation**: GitHub Actions inherently does not trigger workflow runs from events initiated by the built-in `GITHUB_TOKEN`.
3. **Change Detection (`git diff --quiet`)**: If no metrics or problems changed, the workflow exits `0` without committing.
4. **Concurrency Control**:
   ```yaml
   concurrency:
     group: update-readme
     cancel-in-progress: false
   ```
   Ensures that consecutive pushes are queued and executed sequentially without merge conflicts.

---

## 3. Required GitHub Repository Settings

To allow GitHub Actions to commit the updated `README.md` back to your repository:

1. Navigate to your repository on GitHub:
   ```text
   https://github.com/NguyenVinhHung2705/ICPC_/settings/actions
   ```
2. Under **Workflow permissions**:
   - Select **Read and write permissions**
   - Check **Allow GitHub Actions to create and approve pull requests** (optional, recommended)
3. Click **Save**.

> [!NOTE]
> The workflow uses the built-in `GITHUB_TOKEN` with `permissions: contents: write`. No Personal Access Token (PAT) is required, eliminating credential exposure risks.

---

## 4. How to Manually Trigger the Cloud Workflow

You can run the synchronization at any moment via the GitHub web interface:

1. Open your repository on GitHub: `https://github.com/NguyenVinhHung2705/ICPC_`.
2. Click the **Actions** tab.
3. In the left sidebar, click **Immediate README Synchronization**.
4. Click the **Run workflow** dropdown on the right.
5. Select branch `main` and click **Run workflow**.

Using the GitHub CLI (`gh`):
```bash
gh workflow run update-readme.yml
```

---

## 5. Inspecting Cloud Execution Logs

1. Go to the **Actions** tab on GitHub.
2. Click on the latest workflow run (e.g., `Immediate README Synchronization #1`).
3. Click on the **Synchronize README.md** job.
4. Expand the **Execute README updater** or **Commit and push changes** step to view the detailed summary:
   ```text
   ========================================
          README SYNCHRONIZATION
   ========================================
   Total source files:       19 -> 20
   Unique problems:          18 -> 19
   C++ solutions:            17 -> 18
   Python solutions:          2 -> 2

   New problems detected:
     + 1000_123A.cpp

   Modified sections:
     - Directory Structure
     - Rating Progression & Problem Collection
     - Repository Metrics
     - Verified Solution Archive

   README successfully synchronized.
   ========================================
   ```

---

## 6. Local Execution & Offline Development

You can also run the exact same updater on your local machine before pushing:

### Requirements
- Python 3.9+
- `requests` package:
  ```bash
  pip install -r requirements.txt
  ```

### CLI Commands

```bash
# Standard update: scans repo and updates README.md
python scripts/update_readme.py

# Dry-run: view proposed changes without modifying README.md
python scripts/update_readme.py --dry-run

# Verification check: exits with 0 if synchronized, 1 if out of sync
python scripts/update_readme.py --check

# Force refresh metadata from Codeforces API
python scripts/update_readme.py --refresh-cache
```

### Pre-Push Git Hook (Optional Local Guard)

To catch unsynchronized solutions locally before pushing:

```bash
# Install hook
python scripts/install_hooks.py

# Uninstall hook if needed
python scripts/install_hooks.py --uninstall
```

When installed, running `git push` checks whether `README.md` is up to date. If solutions were added without updating `README.md`, it updates `README.md` and pauses the push so you can review and stage the changes.

---

## 7. Adding New Solutions & Directory Conventions

### Naming Pattern
```text
<rating>/<rating>_<problem_code>.<extension>
```

### Examples:
- C++ solution: `800/800_112A.cpp`
- Python solution: `900/900_208A.py`
- Starting a new tier: `1100/1100_158B.cpp`

### Dual Implementations:
If a problem is solved in both C++ and Python (e.g. `900_208A.cpp` and `900_208A.py`):
- Counted as **2 solution files**.
- Counted as **1 unique problem**.
- Rendered in a single row with links joined by ` \| ` and language displayed as `C++20 / Python 3`.

---

## 8. Metadata Retrieval & Resilience Guarantees

1. **Local Disk Cache (`metadata/problems_cache.json`)**:
   Contains verified problem titles, ratings, tags, and URLs. If a problem is cached, no network request is made.
2. **Official Codeforces API**:
   New problems are queried against `https://codeforces.com/api/problemset.problems`.
3. **Graceful Degradation (Offline / Maintenance)**:
   If Codeforces API is down, rate-limited, or blocked:
   - Existing verified titles from `README.md` and `problems_cache.json` are preserved.
   - For unknown problems, title falls back to `Not retrieved` without crashing or inventing fake names.
   - No broken links are generated.
4. **Atomic Write Safety**:
   The updater writes to `README.md.tmp` and replaces `README.md` atomically. If any error occurs during generation, your existing `README.md` remains untouched.

---

## 9. Day-to-Day Developer Experience

With Immediate Cloud Automation configured, your workflow is frictionless:

```text
1. Solve a problem (e.g., create 1100/1100_158B.cpp)
2. Commit: git add 1100/ && git commit -m "feat(1100): solve 158B"
3. Push: git push origin main
4. Done!
   GitHub Actions immediately triggers in the cloud:
     - Scans the newly pushed solution
     - Fetches official problem metadata from Codeforces
     - Recalculates metrics and rating distribution
     - Updates README.md
     - Commits: "docs: automatically update README after new solutions"
```
No manual README edits. No bookkeeping mistakes. Total synchronization.
