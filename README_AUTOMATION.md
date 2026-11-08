# Automated README Synchronization System (Local & Cloud GitHub Actions)

This document provides a comprehensive guide to the **Competitive Programming README Automation System** designed for continuous preparation toward **ICPC 2027**.

The automation operates in two complementary modes:
1. **Cloud Automation (GitHub Actions)**: Fully autonomous execution running on GitHub-hosted runners — synchronizes your repository even when your personal computer is powered down, sleeping, or offline.
2. **Local CLI Execution**: On-demand and Git-hook-driven execution for offline development and local validation.

---

## 1. Cloud Automation Architecture (GitHub Actions)

The cloud workflow runs on GitHub-hosted Ubuntu runners, automatically scanning the codebase, recalculating metrics, resolving metadata, and committing updates to `README.md`.

```
               [Daily Schedule: 23:00 ICT (16:00 UTC)]
                                 OR
               [git push to main in [0-9]*/** or scripts/**]
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
                   +-------------------+-------------------+
                   |                                       |
                   | (No changes)                          | (Changes detected)
                   v                                       v
    +-----------------------------+         +-------------------------------+
    | No commit created           |         | Configure git identity:       |
    | Exit 0 (Clean finish)       |         | github-actions[bot]           |
    +-----------------------------+         +---------------+---------------+
                                                            |
                                                            v
                                            +-------------------------------+
                                            | Stage & Commit:               |
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

### 1. Triggers

- **Scheduled Execution (Cron)**:
  Runs daily at **23:00 Vietnam time (UTC+7)**, which corresponds to **16:00 UTC**:
  ```yaml
  schedule:
    - cron: '0 16 * * *'
  ```
- **Push Trigger (Path-Filtered)**:
  Runs automatically whenever new solution files are pushed to `main`:
  ```yaml
  push:
    branches:
      - main
    paths:
      - '[0-9]*/**'    # Triggers on rating folders (800/, 900/, 1000/, etc.)
      - 'scripts/**'   # Triggers on updater script improvements
  ```
- **Manual Trigger (`workflow_dispatch`)**:
  Allows on-demand execution directly from the GitHub web interface or GitHub CLI.

### 2. Concurrency & Infinite Loop Prevention

To guarantee that the automation never runs in infinite execution loops or collides with itself:
1. **Path Filtering**: The push trigger only monitors solution folders (`[0-9]*/**`) and `scripts/**`. It explicitly ignores `README.md`. Therefore, commits pushed by the bot (which only touch `README.md`) will **never** trigger another run.
2. **`GITHUB_TOKEN` Protection**: By design, commits created with the default `GITHUB_TOKEN` do not trigger new workflow runs on push events.
3. **Change Detection (`git diff --quiet`)**: If no documentation changes are produced, the workflow exits cleanly without generating empty commits.
4. **Concurrency Control**:
   ```yaml
   concurrency:
     group: update-readme
     cancel-in-progress: false
   ```
   Ensures that only one synchronization job runs at a time, preventing race conditions.

---

## 3. Required GitHub Repository Settings

To allow GitHub Actions to commit the updated `README.md` back to your repository:

1. Navigate to your repository on GitHub:
   ```text
   https://github.com/NguyenVinhHung2705/ICPC_/settings/actions
   ```
2. Under **Workflow permissions**, verify:
   - Select: **Read and write permissions**
   - Check: **Allow GitHub Actions to create and approve pull requests** (optional, recommended)
3. Click **Save**.

> [!NOTE]
> The workflow uses the built-in `GITHUB_TOKEN` with `permissions: contents: write`. No Personal Access Token (PAT) is required, eliminating credential exposure risks.

---

## 4. How to Manually Trigger the Cloud Workflow

You can run the synchronization at any moment via the GitHub web interface:

1. Open your repository on GitHub: `https://github.com/NguyenVinhHung2705/ICPC_`.
2. Click the **Actions** tab.
3. In the left sidebar, click **Automated README Synchronization**.
4. Click the **Run workflow** dropdown on the right.
5. Select branch `main` and click **Run workflow**.

Using the GitHub CLI (`gh`):
```bash
gh workflow run update-readme.yml
```

---

## 5. Inspecting Cloud Execution Logs

1. Go to the **Actions** tab on GitHub.
2. Click on the latest workflow run (e.g., `Automated README Synchronization #4`).
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

## 9. Typical Cloud-First Workflow

With GitHub Actions enabled, your day-to-day workflow is as simple as:

```text
1. Solve a problem (e.g., create 1000/1000_123A.cpp)
2. Commit: git add 1000/ && git commit -m "feat(1000): solve 123A"
3. Push: git push origin main
4. Done!
   GitHub Actions automatically:
     - Scans the new solution
     - Fetches problem metadata
     - Updates README.md statistics
     - Commits: "docs: automatically synchronize README statistics"
```
Even if you push from a mobile device or web editor, or if your PC is shut down, GitHub Actions keeps your archive documentation synchronized and pristine.
