# Competitive Programming Journey

<div align="center">

[![C++](https://img.shields.io/badge/C%2B%2B-17%20%2F%2020-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)](https://en.cppreference.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codeforces](https://img.shields.io/badge/Codeforces-Practice-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/)
[![LeetCode](https://img.shields.io/badge/LeetCode-NguyenVinhHung2705-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/NguyenVinhHung2705/)
[![Target](https://img.shields.io/badge/Roadmap-ICPC%202027-E91E63?style=for-the-badge)](./COMPETITIVE_PROGRAMMING_ROADMAP.md)

<br/>

**"Every problem solved is a step closer to becoming a better problem solver."**

*A disciplined archive of algorithmic development, mathematical reasoning, and continuous preparation for ICPC 2027.*

<br/>

</div>

---

## Table of Contents

- [About Me](#about-me)
- [Repository Overview](#repository-overview)
- [Directory Structure & Conventions](#directory-structure--conventions)
- [Rating Progression & Problem Collection](#rating-progression--problem-collection)
- [Algorithmic Paradigms & Core Topics](#algorithmic-paradigms--core-topics)
- [Online Judges & Practice Ecosystem](#online-judges--practice-ecosystem)
- [Problem Solving & Learning Philosophy](#problem-solving--learning-philosophy)
- [The ICPC 2027 Roadmap](#the-icpc-2027-roadmap)
- [Repository Companion Curriculum](#repository-companion-curriculum)
- [Profiles & Contact](#profiles--contact)

---

## About Me

I am **Nguyễn Vĩnh Hưng**, a Computer Science / Information Technology student passionate about algorithms, discrete mathematics, and computational problem solving.

This repository serves as my structured training ground. Rather than practicing aimlessly or memorizing standard solution templates, my focus is centered on cultivating deep analytical intuition: breaking down complex problem constraints, discovering underlying invariants, proving algorithm correctness, and implementing optimal, bug-free code under competitive constraints.

### Core Objectives
- **Algorithmic & Mathematical Rigor**: Develop strong pattern recognition across dynamic programming, number theory, graph theory, and combinatorics.
- **Systematic Problem Solving**: Transform high-level intuition into mathematically sound, asymptotically optimal implementations.
- **Competitive Contest Readiness**: Hone speed, implementation precision, and psychological endurance for timed contests.
- **The Long-Term Mission**: Return to the ICPC arena in **2027** with significant algorithmic depth, mental resilience, and technical maturity.

> *"I am not collecting solutions. I am building problem-solving skills."*

---

## Repository Overview

This repository documents my continuous journey across competitive programming platforms, with an emphasis on **Codeforces**, complemented by curated problem sets from **CSES**, **AtCoder**, **VNOI**, and **LeetCode**.

- **Primary Languages**:
  - **C++ (C++17 / C++20)**: Main competitive language. Leverages the standard template library (STL), fast input/output routines, and cache-friendly data structures.
  - **Python (Python 3)**: Employed for rapid prototyping, ad-hoc string parsing, and problems requiring arbitrary-precision arithmetic.
- **Key Tenets**:
  - **Code Quality**: Clean structure, meaningful variable naming, and clear algorithmic logic.
  - **Constraint-Driven Design**: Solutions engineered specifically to satisfy strict time and memory bounds.
  - **Continuous Iteration**: Re-evaluating past solutions with cleaner, more optimal techniques as my skill level expands.

---

## Directory Structure & Conventions

Problems are categorized into dedicated directories matching their **Codeforces problem difficulty rating**.

<!-- AUTO-GEN:DIRECTORY_STRUCTURE:START -->
```text
Competitive-Programming/
├── .github/workflows/                    # GitHub Actions CI/CD automation
│   └── update-readme.yml                 # Immediate push-triggered README sync
├── 800/                                  # Rating 800: Basic implementation & simulation
│   ├── 800_50A.cpp
│   ├── 800_112A.cpp
│   ├── 800_158A.cpp
│   ├── 800_236A.cpp
│   └── ...
├── 900/                                  # Rating 900: Elementary observations & brute force
│   ├── 900_96A.cpp
│   ├── 900_133A.cpp
│   ├── 900_160A.cpp
│   ├── 900_208A.cpp
│   └── ...
├── 1000/                                 # Rating 1000: Basic algorithms & greedy logic
│   ├── 1000_90A.cpp
│   ├── 1000_967B.cpp
│   ├── 1000_979A.cpp
│   └── 1000_1346A.cpp
├── 1100/                                 # Rating 1100: Pattern recognition (Active target)
├── 1200/                                 # Rating 1200: Foundational algorithms (Active target)
├── ...                                   # Scalable hierarchy up to 2000+
├── metadata/                             # Local problem metadata & API cache
│   └── problems_cache.json               # Offline problem definitions & tags
├── scripts/                              # Repository automation & README sync engine
│   ├── codeforces_api.py                 # Codeforces API client & cache resolver
│   ├── config.py                         # Configurations & language definitions
│   ├── install_hooks.py                  # Local Git pre-push hook manager
│   └── update_readme.py                  # Main synchronization script
├── COMPETITIVE_PROGRAMMING_ROADMAP.md    # In-depth 14-chapter curriculum & theoretical syllabus
├── README_AUTOMATION.md                  # Comprehensive automation guide & workflows
├── requirements.txt                      # Python dependencies (requests)
├── .gitignore                            # Standard build & binary exclusion rules
└── README.md                             # Repository documentation
```
<!-- AUTO-GEN:DIRECTORY_STRUCTURE:END -->

### File Naming Convention

Every solution follows a standardized, machine-readable format:

```text
<rating>_<problem_code>.<extension>
```

**Example**: `1000/1000_90A.cpp`
- `<rating>`: Problem difficulty rating assigned by Codeforces.
- `<problem_code>`: Official Codeforces problem identifier (Contest `90`, Problem `A`).
- `.<extension>`: Implementation language source file (`.cpp` or `.py`).

> **Note**: Directory tiers reflect the **inherent difficulty of the problems**, not personal user rating.

---

## Rating Progression & Problem Collection

The tier hierarchy serves as a progressive training benchmark. Each rating bracket isolates specific cognitive hurdles and implementation skills:

<!-- AUTO-GEN:RATING_TABLE:START -->
| Rating Tier | Difficulty Level | Primary Cognitive Focus | Status |
| :---: | :---: | :--- | :---: |
| **800** | Beginner | Basic implementation, condition checking, array manipulation | [9 Solved](./800/) |
| **900** | Beginner | Elementary problem solving, basic math, brute-force reasoning | [10 Solved (11 files)](./900/) |
| **1000** | Elementary | Basic algorithms, greedy observations, coordinate transformations | [4 Solved](./1000/) |
| **1100** | Elementary | Pattern recognition, sorting techniques, number theory basics | *In Progress* |
| **1200** | Intermediate | Algorithmic thinking, prefix sums, two pointers, binary search | *Target* |
| **1300** | Intermediate | Greedy strategies, constructive algorithms, state space search | *Target* |
| **1400** | Intermediate | Deeper problem solving, binary search on answer, elementary DP | *Target* |
| **1500** | Advanced | Combinatorics, graph traversals (BFS/DFS), modular arithmetic | *Target* |
| **1600** | Advanced | Stronger mathematical reasoning, trees, segment trees, game theory | *Target* |
| **1700–1900** | Advanced | Complex algorithms, flow networks, DP optimizations, advanced DS | *Target* |
| **2000+** | Expert | Master-level reductions, advanced graph theory, ICPC Regional sets | *Target* |
<!-- AUTO-GEN:RATING_TABLE:END -->

### Current Repository Metrics

<!-- AUTO-GEN:METRICS:START -->
*Statistics verified directly from current workspace source files:*

- **Total Solutions Stored**: 24 files
- **Unique Problems Solved**: 23
- **Language Distribution**:
  - **C++ (C++17 / C++20)**: 22 solutions
  - **Python (Python 3)**: 2 solutions
- **Rating Distribution**:
  - **800**: 9 solutions
  - **900**: 10 unique problems (9 C++, 2 Python — *208A implemented in both languages*)
  - **1000**: 4 solutions
<!-- AUTO-GEN:METRICS:END -->

### Verified Solution Archive

<!-- AUTO-GEN:ARCHIVE:START -->
<details open>
<summary><b>Click to expand / collapse full problem index (23 problems)</b></summary>

<br/>

| Rating | Code | Problem Title | Solution | Language | Platform Link |
| :---: | :---: | :--- | :---: | :---: | :---: |
| `800` | **50A** | Domino piling | [`800_50A.cpp`](./800/800_50A.cpp) | C++20 | [Codeforces 50A](https://codeforces.com/problemset/problem/50/A) |
| `800` | **112A** | Petya and Strings | [`800_112A.cpp`](./800/800_112A.cpp) | C++20 | [Codeforces 112A](https://codeforces.com/problemset/problem/112/A) |
| `800` | **158A** | Next Round | [`800_158A.cpp`](./800/800_158A.cpp) | C++20 | [Codeforces 158A](https://codeforces.com/problemset/problem/158/A) |
| `800` | **236A** | Boy or Girl | [`800_236A.cpp`](./800/800_236A.cpp) | C++20 | [Codeforces 236A](https://codeforces.com/problemset/problem/236/A) |
| `800` | **263A** | Beautiful Matrix | [`800_263A.cpp`](./800/800_263A.cpp) | C++20 | [Codeforces 263A](https://codeforces.com/problemset/problem/263/A) |
| `800` | **281A** | Word Capitalization | [`800_281A.cpp`](./800/800_281A.cpp) | C++20 | [Codeforces 281A](https://codeforces.com/problemset/problem/281/A) |
| `800` | **339A** | Helpful Maths | [`800_339A.cpp`](./800/800_339A.cpp) | C++20 | [Codeforces 339A](https://codeforces.com/problemset/problem/339/A) |
| `800` | **617A** | Elephant | [`800_617A.cpp`](./800/800_617A.cpp) | C++20 | [Codeforces 617A](https://codeforces.com/problemset/problem/617/A) |
| `800` | **791A** | Bear and Big Brother | [`800_791A.cpp`](./800/800_791A.cpp) | C++20 | [Codeforces 791A](https://codeforces.com/problemset/problem/791/A) |
| `900` | **96A** | Football | [`900_96A.cpp`](./900/900_96A.cpp) | C++20 | [Codeforces 96A](https://codeforces.com/problemset/problem/96/A) |
| `900` | **133A** | HQ9+ | [`900_133A.cpp`](./900/900_133A.cpp) | C++20 | [Codeforces 133A](https://codeforces.com/problemset/problem/133/A) |
| `900` | **160A** | Twins | [`900_160A.cpp`](./900/900_160A.cpp) | C++20 | [Codeforces 160A](https://codeforces.com/problemset/problem/160/A) |
| `900` | **208A** | Dubstep | [`900_208A.cpp`](./900/900_208A.cpp) \| [`900_208A.py`](./900/900_208A.py) | C++20 / Python 3 | [Codeforces 208A](https://codeforces.com/problemset/problem/208/A) |
| `900` | **318A** | Even Odds | [`900_318A.cpp`](./900/900_318A.cpp) | C++20 | [Codeforces 318A](https://codeforces.com/problemset/problem/318/A) |
| `900` | **337A** | Puzzles | [`900_337A.py`](./900/900_337A.py) | Python 3 | [Codeforces 337A](https://codeforces.com/problemset/problem/337/A) |
| `900` | **405A** | Gravity Flip | [`900_405A.cpp`](./900/900_405A.cpp) | C++20 | [Codeforces 405A](https://codeforces.com/problemset/problem/405/A) |
| `900` | **580A** | Kefa and First Steps | [`900_580A.cpp`](./900/900_580A.cpp) | C++20 | [Codeforces 580A](https://codeforces.com/problemset/problem/580/A) |
| `900` | **1225A** | Forgetting Things | [`900_1225A.cpp`](./900/900_1225A.cpp) | C++20 | [Codeforces 1225A](https://codeforces.com/problemset/problem/1225/A) |
| `900` | **1238A** | Prime Subtraction | [`900_1238A.cpp`](./900/900_1238A.cpp) | C++20 | [Codeforces 1238A](https://codeforces.com/problemset/problem/1238/A) |
| `1000` | **90A** | Cableway | [`1000_90A.cpp`](./1000/1000_90A.cpp) | C++20 | [Codeforces 90A](https://codeforces.com/problemset/problem/90/A) |
| `1000` | **967B** | Watering System | [`1000_967B.cpp`](./1000/1000_967B.cpp) | C++20 | [Codeforces 967B](https://codeforces.com/problemset/problem/967/B) |
| `1000` | **979A** | Pizza, Pizza, Pizza!!! | [`1000_979A.cpp`](./1000/1000_979A.cpp) | C++20 | [Codeforces 979A](https://codeforces.com/problemset/problem/979/A) |
| `1000` | **1346A** | Color Revolution | [`1000_1346A.cpp`](./1000/1000_1346A.cpp) | C++20 | [Codeforces 1346A](https://codeforces.com/problemset/problem/1346/A) |

</details>
<!-- AUTO-GEN:ARCHIVE:END -->

---

## Algorithmic Paradigms & Core Topics

Problems in this repository are analyzed and solved through core computer science paradigms. The curriculum is mapped systematically against our [Competitive Programming Roadmap](./COMPETITIVE_PROGRAMMING_ROADMAP.md):

```
                     ┌───────────────────────────────────┐
                     │   Competitive Programming Stack   │
                     └─────────────────┬─────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
 ┌──────┴─────────┐            ┌───────┴────────┐            ┌────────┴────────┐
 │  Paradigms     │            │ Data Structures│            │   Mathematics   │
 ├────────────────┤            ├────────────────┤            ├─────────────────┤
 │ • Complete     │            │ • STL Vectors  │            │ • Number Theory │
 │   Search       │            │   & Maps       │            │ • Modular Math  │
 │ • Two Pointers │            │ • Disjoint Set │            │ • Combinatorics │
 │ • Sliding Win. │            │   Union (DSU)  │            │ • Pigeonhole    │
 │ • Binary Search│            │ • Fenwick Tree │            │ • Parity &      │
 │ • Greedy Obs.  │            │ • Segment Tree │            │   Invariants    │
 │ • Dynamic Prog.│            │ • Monotonic    │            │ • Matrix Exp.   │
 │ • Graph Search │            │   Queue/Stack  │            │ • Bitwise Logic │
 └────────────────┘            └────────────────┘            └─────────────────┘
```

- **Fundamental Logic & Ad-Hoc**: Clean implementation, state simulation, constructive algorithms, invariant detection.
- **Search & Optimization**: Binary search on answer, two pointers, sliding window, prefix sums, meet-in-the-middle.
- **Dynamic Programming**: State modeling, transitions, 1D/2D table design, memory optimization, bitmask DP.
- **Data Structures**: Standard Template Library containers, Monotonic Stacks/Queues, Disjoint Set Union (DSU), Binary Indexed Trees (Fenwick), Segment Trees with Lazy Propagation.
- **Graph Theory**: Graph modeling, Breadth-First Search (unweighted shortest path), Depth-First Search, topological sorting, cycle detection.
- **Mathematical Foundations**: Prime factorization, Euclidean algorithm (GCD/LCM), modular inverses, combinatorics, inclusion-exclusion principle.

---

## Online Judges & Practice Ecosystem

To ensure comprehensive algorithmic exposure, practice is conducted across established competitive programming judges:

| Platform | Role in Training | Direct Link |
| :--- | :--- | :---: |
| **Codeforces** | Primary platform for timed contest simulations, speed, and rating benchmarks | [codeforces.com](https://codeforces.com/) |
| **VNOI Online Judge** | High-quality Vietnamese contest archive, Olympic, and ICPC regional preparation | [oj.vnoi.info](https://oj.vnoi.info/) |
| **CSES Problem Set** | Standardized algorithmic reference tasks across dynamic programming, trees, and graphs | [cses.fi](https://cses.fi/problemset/) |
| **AtCoder** | Deep mathematical reasoning, elegant constructive challenges, and ABC/ARC contests | [atcoder.jp](https://atcoder.jp/) |
| **LeetCode** | Data structure mastery, algorithmic patterns, and interview-grade problem solving | [leetcode.com](https://leetcode.com/) |

---

## Problem Solving & Learning Philosophy

> *"I don't practice to memorize solutions. I practice to recognize patterns, understand problems, and build better solutions."*

Solving a competitive programming problem is an engineering process governed by 8 non-negotiable principles:

1. **Understand Before Coding**  
   Read the problem statement thoroughly. Manually simulate all sample tests and edge cases on paper before touching the keyboard.
2. **Analyze Constraints First**  
   Identify the magnitude of `N`, `M`, and `K`. Let constraint limits dictate the permissible asymptotic time complexity (`O(N)`, `O(N log N)`, `O(N^2)`).
3. **Start with Brute Force**  
   Formulate the naive approach first. Understanding the complete state space is the fastest path to discovering redundancies.
4. **Identify the Key Observation**  
   Look for monotonicity, symmetry, mathematical invariants, or greedy local optimality that collapses the problem space.
5. **Optimize Systematically**  
   Replace naive searches with binary search, precomputation (prefix sums), or specialized data structures (Fenwick/Segment trees).
6. **Prove Correctness Before Submitting**  
   Ensure the approach holds for extreme bounds (`N = 1`, empty inputs, maximum constraint values, overflow risks requiring 64-bit integer `long long`).
7. **Perform Post-Mortem Reviews**  
   For every wrong answer (WA) or time limit exceeded (TLE), analyze the flawed assumption. Compare implementations with top contestant editorials.
8. **Revisit Difficult Problems**  
   Re-solve challenging problems after 7–14 days without looking at notes to ensure concept internalisation.

---

## The ICPC 2027 Roadmap

The journey toward ICPC 2027 is a marathon structured into four distinct, measurable phases:

```
2026 Q1-Q2                      2026 Q3-Q4                      2026 Q4 - 2027 Q1               2027
┌──────────────────────┐        ┌──────────────────────┐        ┌──────────────────────┐        ┌──────────────────────┐
│  Phase 1: Foundation │───────>│  Phase 2: Core Parad.│───────>│  Phase 3: Adv Topics │───────>│  Phase 4: ICPC Prep │
│  • Rating 800 - 1200 │        │  • Rating 1300 - 1600│        │  • Rating 1700 - 1900│        │  • Rating 2000+      │
│  • Fast I/O & STL    │        │  • Math & Greedy     │        │  • SegTree, DSU, DP  │        │  • Virtual Contests  │
│  • Clean Simulation  │        │  • Two Pointers & BS │        │  • Dec 2026 Contests │        │  • ICPC Regionals    │
└──────────────────────┘        └──────────────────────┘        └──────────────────────┘        └──────────────────────┘
```

- **Phase 1: Foundations & Implementation Rigor** *(Current Focus)*
  - Stabilize Codeforces ratings 800 to 1200.
  - Zero-penalty speed on implementation, basic math, and foundational search logic.
- **Phase 2: Algorithmic Paradigms & Mathematical Intuition**
  - Target ratings 1300 to 1600.
  - Deepen dynamic programming transitions, number theory, greedy proofs, and binary search on answers.
- **Phase 3: Advanced Data Structures & Contest Endurance**
  - Target ratings 1700 to 1900.
  - Fluency in segment trees with lazy propagation, Fenwick trees, DSU, and graph algorithms.
  - Targeted participation in university selection contests (December 2026 milestone).
- **Phase 4: High-Performance ICPC Regional Readiness (2027)**
  - Reach and maintain 2000+ rating competency.
  - Team coordination, 5-hour endurance contests, and competitive execution at the **ICPC Regional 2027**.

---

## Repository Companion Curriculum

For a comprehensive breakdown of theoretical foundations, algorithmic templates, and chapter-by-chapter study plans, consult the dedicated repository guide:

📖 **[COMPETITIVE_PROGRAMMING_ROADMAP.md](./COMPETITIVE_PROGRAMMING_ROADMAP.md)**
- *Chapter 1: Problem Solving Thinking (Brute force, Constraints, Patterns, Invariants)*
- *Chapter 2: Mathematical Thinking (Number theory, Combinatorics, Matrix exponentiation)*
- *Chapter 3: Algorithm Paradigms (Binary search, DP deep-dive, Two pointers)*
- *Chapter 4: Data Structures (Modern STL, Monotonic queues, Fenwick & Segment trees)*
- *Chapter 5–14: Advanced Graph Theory, Geometry, String Algorithms, and Contest Strategies*

---

## Profiles & Contact

- **GitHub**: [@NguyenVinhHung2705](https://github.com/NguyenVinhHung2705)
- **LeetCode**: [@NguyenVinhHung2705](https://leetcode.com/NguyenVinhHung2705/)
- **Repository Remote**: [github.com/NguyenVinhHung2705/ICPC_](https://github.com/NguyenVinhHung2705/ICPC_)

---

<div align="center">

**"ICPC is not the finish line. It is the challenge that keeps me moving forward."**

*One problem at a time. One improvement at a time. Until ICPC.*

</div>

