# GIÁO TRÌNH HUẤN LUYỆN COMPETITIVE PROGRAMMING TOÀN DIỆN
## LỘ TRÌNH CHINH PHỤC KỲ THI TIN HỌC 12/2026 VÀ ICPC 2027

> **Tài liệu độc bản dành riêng cho lập trình viên thi đấu (Competitive Programmer)**
> **Ngôn ngữ triển khai:** C++17 / C++20
> **Định hướng cốt lõi:** Phát triển tư duy toán học, nhận diện mô hình bài toán (Pattern Recognition), chứng minh thuật toán và tư duy giải quyết vấn đề độc lập trước các bài toán chưa từng gặp.

---

## MỤC LỤC TỔNG QUAN

1. [CHƯƠNG 1: PROBLEM SOLVING THINKING (TƯ DUY GIẢI QUYẾT VẤN ĐỀ)](#chương-1-problem-solving-thinking)
   - [1.1. Brute Force Thinking (Tư duy Vét cạn & Không gian nghiệm)](#11-brute-force-thinking)
   - [1.2. Constraint-Based Thinking (Tư duy dựa trên Giới hạn)](#12-constraint-based-thinking)
   - [1.3. Pattern Recognition (Tư duy Nhận diện Khuôn mẫu)](#13-pattern-recognition)
   - [1.4. Mathematical Observation (Quan sát Bản chất Toán học)](#14-mathematical-observation)
   - [1.5. Invariant Thinking (Tư duy Bất biến)](#15-invariant-thinking)
   - [1.6. Greedy Thinking (Tư duy Tham lam & Điều kiện Tối ưu địa phương)](#16-greedy-thinking)
   - [1.7. Divide and Conquer (Tư duy Chia để trị)](#17-divide-and-conquer)
   - [1.8. Reverse Thinking (Tư duy Đảo ngược bài toán)](#18-reverse-thinking)
   - [1.9. Constructive Thinking (Tư duy Kiến tạo nghiệm)](#19-constructive-thinking)
   - [1.10. Reduction Thinking (Tư duy Quy nạp & Thu gọn bài toán)](#110-reduction-thinking)
   - [1.11. State Modeling (Tư duy Mô hình hóa Trạng thái)](#111-state-modeling)
   - [1.12. Graph Modeling (Tư duy Đồ thị hóa bài toán thực tế)](#112-graph-modeling)
   - [1.13. Optimization Thinking (Tư duy Tối ưu hóa tiệm tiến)](#113-optimization-thinking)
   - [1.14. Proof of Correctness (Tư duy Chứng minh tính đúng đắn)](#114-proof-of-correctness)
2. [CHƯƠNG 2: MATHEMATICAL THINKING (TƯ DUY TOÁN HỌC TRONG CP)](#chương-2-mathematical-thinking)
   - [2.1. Number Theory (Số học chuyên sâu)](#21-number-theory)
   - [2.2. Combinatorics (Tổ hợp & Đếm nâng cao)](#22-combinatorics)
   - [2.3. Principles: Pigeonhole, PIE & Induction](#23-principles-pigeonhole-pie--induction)
   - [2.4. Probability & Expected Value (Xác suất & Kỳ vọng)](#24-probability--expected-value)
   - [2.5. Bit Manipulation & Linear Basis (Thao tác Bit & Không gian Vector GF(2))](#25-bit-manipulation--linear-basis)
   - [2.6. Matrix Exponentiation (Lũy thừa ma trận & Hệ thức truy hồi)](#26-matrix-exponentiation)
   - [2.7. Invariant, Parity & Algebraic Transformations](#27-invariant-parity--algebraic-transformations)
   - [2.8. Nhận biết bài toán thuần Toán học (No-Algorithm Problem)](#28-nhận-biết-bài-toán-thuần-toán-học)
3. [CHƯƠNG 3: ALGORITHM PARADIGMS (CÁC MÔ HÌNH THUẬT TOÁN KINH ĐIỂN)](#chương-3-algorithm-paradigms)
   - [3.1. Brute Force, Recursion & Backtracking Pruning](#31-brute-force-recursion--backtracking-pruning)
   - [3.2. Divide and Conquer & Meet-in-the-Middle](#32-divide-and-conquer--meet-in-the-middle)
   - [3.3. Binary Search on Answer & Monotonicity](#33-binary-search-on-answer--monotonicity)
   - [3.4. Two Pointers & Sliding Window](#34-two-pointers--sliding-window)
   - [3.5. Sweep Line & Offline Queries](#35-sweep-line--offline-queries)
   - [3.6. Dynamic Programming Deep Dive (Quy hoạch động chuyên sâu)](#36-dynamic-programming-deep-dive)
   - [3.7. Specialized DP: Bitmask, Digit, Tree & Rerooting](#37-specialized-dp-bitmask-digit-tree--rerooting)
   - [3.8. DP Optimization Techniques (Tối ưu hóa QHĐ)](#38-dp-optimization-techniques)
4. [CHƯƠNG 4: DATA STRUCTURES (CẤU TRÚC DỮ LIỆU TỪ CƠ BẢN ĐẾN CAO CẤP)](#chương-4-data-structures)
   - [4.1. Modern C++ STL & Custom Allocators / Hash](#41-modern-c-stl)
   - [4.2. Monotonic Stack & Monotonic Queue](#42-monotonic-stack--monotonic-queue)
   - [4.3. Disjoint Set Union (DSU) & Rollback DSU](#43-disjoint-set-union-dsu)
   - [4.4. Fenwick Tree (Binary Indexed Tree)](#44-fenwick-tree)
   - [4.5. Segment Tree & Lazy Propagation](#45-segment-tree--lazy-propagation)
   - [4.6. Sparse Table & Binary Lifting](#46-sparse-table--binary-lifting)
   - [4.7. Trie & Binary Trie](#47-trie--binary-trie)
   - [4.8. Ordered Set (`__gnu_pbds`)](#48-ordered-set)
   - [4.9. Persistent Segment Tree](#49-persistent-segment-tree)
5. [CHƯƠNG 5: GRAPH ALGORITHMS (THUẬT TOÁN ĐỒ THỊ)](#chương-5-graph-algorithms)
   - [5.1. Graph Traversals & Topological Ordering](#51-graph-traversals--topological-ordering)
   - [5.2. Shortest Paths: Dijkstra, 0-1 BFS, Bellman-Ford, Floyd-Warshall](#52-shortest-paths)
   - [5.3. Minimum Spanning Tree: Kruskal & Prim](#53-minimum-spanning-tree)
   - [5.4. Connectivity: Tarjan SCC, Bridges, Articulation Points](#54-connectivity-tarjan-scc-bridges-articulation-points)
   - [5.5. Tree Algorithms: Diameter, LCA, Euler Tour, Tree Flattening](#55-tree-algorithms)
   - [5.6. Network Flow & Bipartite Matching: Dinic & Hopcroft-Karp](#56-network-flow--bipartite-matching)
   - [5.7. 2-Satisfiability (2-SAT)](#57-2-satisfiability-2-sat)
6. [CHƯƠNG 6: STRING ALGORITHMS (THUẬT TOÁN XỬ LÝ CHUỖI)](#chương-6-string-algorithms)
   - [6.1. String Hashing (Polynomial Rolling Hash & Anti-Hash Protection)](#61-string-hashing)
   - [6.2. KMP (Knuth-Morris-Pratt) & Prefix Function](#62-kmp)
   - [6.3. Z-Algorithm](#63-z-algorithm)
   - [6.4. Aho-Corasick Automaton](#64-aho-corasick-automaton)
   - [6.5. Suffix Array & LCP Array](#65-suffix-array--lcp-array)
   - [6.6. Manacher's Algorithm for Palindromes](#66-manachers-algorithm)
7. [CHƯƠNG 7: ADVANCED TOPICS (CHỦ ĐỀ CHUYÊN SÂU & PHÂN TẦNG THI ĐẤU)](#chương-7-advanced-topics)
   - [7.1. Phân tầng kiến thức: Tháng 12/2026 vs ICPC 2027](#71-phân-tầng-kiến-thức)
   - [7.2. Computational Geometry (Hình học tính toán)](#72-computational-geometry)
   - [7.3. Advanced DP Optimizations: CHT & D&C Optimization](#73-advanced-dp-optimizations)
   - [7.4. Heavy-Light Decomposition (HLD) & Centroid Decomposition](#74-heavy-light-decomposition--centroid-decomposition)
   - [7.5. Mo's Algorithm & Square Root Decomposition](#75-mos-algorithm)
   - [7.6. FFT / NTT (Biến đổi Fourier nhanh & Tích chập đa thức)](#76-fft--ntt)
8. [CHƯƠNG 8: CONTEST STRATEGY (CHIẾN THUẬT THI ĐẤU & TÂM LÝ ICPC)](#chương-8-contest-strategy)
   - [8.1. Đọc đề, Phân loại bài và Đọc hiểu Constraints](#81-đọc-đề-và-phân-tích-constraints)
   - [8.2. Kỹ thuật Debugging đỉnh cao: Assertions, Sanitizers & Stress Testing](#82-debugging-stress-testing)
   - [8.3. Tạo Bộ sinh Test Ngẫu nhiên (Random Test Generator)](#83-random-test-generator)
   - [8.4. Chiến thuật thi đấu ICPC đồng đội (3 người - 1 máy tính)](#84-chiến-thuật-icpc-đồng-đội)
9. [CHƯƠNG 9: PATTERN RECOGNITION (BẢNG TRA CỨU NHẬN DIỆN MÔ HÌNH THUẬT TOÁN)](#chương-9-pattern-recognition)
   - [9.1. Ma trận nhận diện theo Constraints & Dấu hiệu bài toán](#91-ma-trận-nhận-diện)
   - [9.2. Phân tích đối chiếu các cặp bài toán dễ gây nhầm lẫn](#92-phân-tích-đối-chiếu-các-cặp-bài-toán-dễ-nhầm-lẫn)
10. [CHƯƠNG 10: ONLINE JUDGE PRACTICE (NGÂN HÀNG BÀI TẬP THỰC TẾ ĐÃ XÁC MINH)](#chương-10-online-judge-practice)
    - [10.1. Hệ thống bài tập Level 1: Fundamental](#101-level-1-fundamental)
    - [10.2. Hệ thống bài tập Level 2: Intermediate](#102-level-2-intermediate)
    - [10.3. Hệ thống bài tập Level 3: Advanced / ICPC](#103-level-3-advanced--icpc)
11. [CHƯƠNG 11: TRAINING ROADMAP (LỘ TRÌNH HUẤN LUYỆN 11/2026 - ICPC 2027)](#chương-11-training-roadmap)
    - [11.1. Phase 1: Nước rút kỳ thi tháng 12/2026](#111-phase-1-nước-rút-122026)
    - [11.2. Phase 2: Củng cố nền tảng Toán học & Thuật toán lõi (01/2027 - 03/2027)](#112-phase-2-củng-cố-nền-tảng)
    - [11.3. Phase 3: Nâng cấp Cấu trúc dữ liệu & Thuật toán nâng cao (04/2027 - 07/2027)](#113-phase-3-nâng-cấp-nâng-cao)
    - [11.4. Phase 4: Luyện đề ICPC Regional & Phối hợp đội tuyển (08/2027 - 09/2027)](#114-phase-4-luyện-đề-icpc)
    - [11.5. Phase 5: Contest Simulation & Đạt điểm rơi phong độ (10/2027 - 11/2027)](#115-phase-5-contest-simulation)
12. [CHƯƠNG 12: PROBLEM ANALYSIS TEMPLATE (KHUNG PHÂN TÍCH BÀI TOÁN CHUẨN MỰC)](#chương-12-problem-analysis-template)
    - [12.1. Quy trình 13 bước chuẩn mực](#121-quy-trình-13-bước)
    - [12.2. Ví dụ thực hành phân tích hoàn chỉnh từ đề bài đến mã nguồn](#122-ví-dụ-thực-hành-phân-tích-hoàn-chỉnh)
13. [CHƯƠNG 13: SELF-ASSESSMENT & PROGRESS TRACKING (HỆ THỐNG CHECKLIST TỰ ĐÁNH GIÁ)](#chương-13-self-assessment--progress-tracking)

---

# TRIẾT LÝ HUẤN LUYỆN CỐT LÕI

Trong Competitive Programming (CP) đỉnh cao, sự khác biệt giữa một thí sinh dừng lại ở mức trung bình và một Grandmaster/ICPC World Finalist **không nằm ở số lượng thuật toán thuộc lòng**, mà nằm ở:
1. **Khả năng quan sát bản chất toán học** ẩn sau câu chuyện của đề bài.
2. **Quy trình tư duy có cấu trúc**: Không bao giờ code ngay khi vừa đọc xong đề. Luôn đi từ Brute Force $\to$ Xác định nút thắt $\to$ Khai thác tính chất bất biến/đơn điệu $\to$ Thuật toán tối ưu $\to$ Chứng minh tính đúng $\to$ Cài đặt chuẩn xác trong 1 lần duy nhất.
3. **Phản xạ nhận diện mô hình (Pattern Recognition)**: Đọc giới hạn thời gian và ràng buộc ($N \le 20$, $N \le 2000$, $N \le 2 \cdot 10^5$, $N \le 10^{18}$) để giới hạn ngay lập tức không gian thuật toán khả thi.
4. **Tâm lý thi đấu vững vàng**: Khả năng tự gỡ rối (unstick) khi thuật toán sai hoặc TLE/WA, sử dụng Stress Testing như một vũ khí tự động tìm test sai trong vòng 3 phút.

---

# CHƯƠNG 1: PROBLEM SOLVING THINKING

> *"Trước khi tìm kiếm thuật toán, hãy tìm kiếm cấu trúc của bài toán."*

Để giải quyết một bài toán mà bạn chưa từng thấy trước đây, bạn không thể trông chờ vào việc "đã từng làm bài tương tự". Bạn cần một bộ công cụ tư duy gồm 14 mô hình tư duy nền tảng sau đây:

---

## 1.1. Brute Force Thinking (Tư duy Vét cạn & Không gian nghiệm)

### 1. Định nghĩa
Brute Force Thinking (Tư duy Vét cạn) là phương pháp tiếp cận đầu tiên đối với mọi bài toán, trong đó ta liệt kê toàn bộ không gian trạng thái (State Space) hoặc không gian nghiệm có thể có để kiểm tra nghiệm thỏa mãn hoặc tìm nghiệm tối ưu nhất.

### 2. Bản chất
Bản chất của Brute Force là xây dựng một **hàm kiểm tra tính đúng** (Oracle/Verifier) và duyệt qua tập hợp hữu hạn $S$ chứa tất cả các cấu hình có thể có của bài toán. Độ phức tạp tỉ lệ thuận với kích thước $|S|$.

### 3. Khi nào sử dụng?
- Luôn luôn là bước đầu tiên trong quá trình nháp để hiểu đề bài một cách sâu sắc nhất.
- Khi $N$ rất nhỏ ($N \le 10$ với $O(N!)$, $N \le 20$ với $O(2^N)$).
- Làm giải pháp đối chứng (Generator & Brute Force Solution) để chạy Stress Test tìm test sai cho thuật toán tối ưu.

### 4. Dấu hiệu nhận biết
- Đề bài yêu cầu: "Tìm tập hợp con...", "Tìm hoán vị...", "Có bao nhiêu cách cấu hình...", với $N \le 22$.
- Khi chưa tìm ra được tính chất toán học hay sự suy giảm không gian trạng thái nào.

### 5. Quy trình suy luận
1. Xác định chính xác cấu trúc một nghiệm: Một tập con? Một hoán vị? Một dãy số?
2. Tính kích thước không gian nghiệm $|S|$: $2^N$, $N!$, $N^K$.
3. Viết đệ quy quay lui (Backtracking) hoặc dùng Bitmask để sinh toàn bộ $|S|$.
4. Kiểm tra từng cấu hình trong thời gian $O(T_{\text{check}})$. Tổng thời gian $O(|S| \cdot T_{\text{check}})$.
5. Quan sát: Có những nhánh nào chắc chắn không dẫn tới kết quả? Đó là tiền đề cho Nhánh cận (Branch and Bound) và Quy hoạch động (DP).

### 6. Ví dụ minh họa
**Bài toán:** Cho mảng $A$ gồm $N$ số nguyên ($N \le 20$). Tìm xem có tồn tại một tập con có tổng bằng đúng $S$ hay không (Subset Sum).
- Không gian nghiệm: $2^N$ tập con. Với $N = 20$, $2^{20} \approx 10^6$, hoàn toàn khả thi trong 1 giây.
- Triển khai Bitmask trong C++:
```cpp
bool hasSubsetSum(const std::vector<int>& a, int target) {
    int n = a.size();
    for (int mask = 0; mask < (1 << n); ++mask) {
        long long current_sum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                current_sum += a[i];
            }
        }
        if (current_sum == target) return true;
    }
    return false;
}
```

### 7. Những trường hợp dễ nhầm lẫn
- Nhầm lẫn giữa $O(2^N)$ (tập con) và $O(N!)$ (hoán vị). Với $N=12$, $2^{12} = 4096$, nhưng $12! \approx 4.79 \cdot 10^8$ (dễ TLE nếu kiểm tra phức tạp).
- Nghĩ rằng Brute Force là tầm thường và bỏ qua bước này. Bỏ qua Brute Force sẽ làm mất đi công cụ stress test cực mạnh sau này.

### 8. Bài tập vận dụng
- [CSES - Apple Division](https://cses.fi/problemset/task/1623) (Độ khó: 1000 - Sinh toàn bộ $2^N$ cách chia táo).
- [Codeforces 550B - Preparing Olympiad](https://codeforces.com/problemset/problem/550/B) (Rating: 1400 - Duyệt tập con bằng Bitmask kết hợp điều kiện).

---

## 1.2. Constraint-Based Thinking (Tư duy dựa trên Giới hạn)

### 1. Định nghĩa
Constraint-Based Thinking là kỹ năng suy ngược thuật toán từ giới hạn của bài toán (Time Limit, Memory Limit, và giá trị cực đại của các biến đầu vào như $N, M, K, A_i$).

### 2. Bản chất
Các giám khảo thiết kế đề bài luôn chọn giới hạn đầu vào sao cho thuật toán đúng (Intended Solution) chạy vừa vặn trong thời gian quy định (thường từ 1.0s đến 2.0s, tương ứng với xấp xỉ $10^8$ phép tính cơ bản trong C++). Ràng buộc chính là "bản đồ chỉ đường" tiết lộ độ phức tạp của thuật toán mục tiêu.

### 3. Khi nào sử dụng?
Ngay sau khi đọc xong đề bài và trước khi bắt đầu nghĩ đến bất kỳ giải pháp thuật toán cụ thể nào.

### 4. Dấu hiệu nhận biết & Bảng đối chiếu vàng
| Giới hạn $N$ | Độ phức tạp mục tiêu khả thi | Hướng thuật toán gợi ý |
| :--- | :--- | :--- |
| $N \le 10 - 11$ | $O(N!)$ hoặc $O(N^2 \cdot 2^N)$ | Quay lui hoán vị, TSP bằng Bitmask DP |
| $N \le 20 - 22$ | $O(2^N)$ hoặc $O(N \cdot 2^N)$ | Duyệt tập con, Bitmask DP, SOS DP |
| $N \le 40$ | $O(2^{N/2})$ | Meet-in-the-Middle |
| $N \le 100$ | $O(N^4)$ hoặc $O(N^3)$ | Floyd-Warshall, Dynamic Programming bậc 3, Khử Gauss |
| $N \le 400 - 500$ | $O(N^3)$ | DP trên ma trận, Luồng cực đại (Dinic / Edmonds-Karp) |
| $N \le 2000 - 5000$ | $O(N^2)$ | Quy hoạch động 2 chiều, Duyệt cặp phần tử, Dijkstra bảng |
| $N \le 10^5 - 2 \cdot 10^5$ | $O(N \log N)$ hoặc $O(N \log^2 N)$ | Segment Tree, Fenwick, Sorting, Binary Search, Divide & Conquer |
| $N \le 10^6$ | $O(N)$ hoặc $O(N \log N)$ | Two Pointers, Monotonic Stack/Queue, Sàng nguyên tố, Hash |
| $N \le 10^9 - 10^{18}$ | $O(\sqrt{N})$, $O(\log N)$, $O(1)$ | Kiểm tra số nguyên tố, Nhân ma trận, Chặt nhị phân, Công thức Toán |

### 5. Quy trình suy luận
1. Đọc giới hạn của $N, M$ và thời gian (ví dụ: $N \le 2 \cdot 10^5$, Time: 1.0s).
2. Tính số phép tính tối đa: $10^8$ phép tính/giây.
3. Loại bỏ các thuật toán có độ phức tạp cao hơn giới hạn: Không thể dùng $O(N^2)$ vì $(2 \cdot 10^5)^2 = 4 \cdot 10^{10} \gg 10^8$.
4. Định hình không gian tìm kiếm thuật toán: Chỉ được chọn các thuật toán $O(N)$ hoặc $O(N \log N)$.
5. Kiểm tra giới hạn bộ nhớ (Memory Limit): 256MB cho phép cấp phát tối đa khoảng $6 \cdot 10^7$ phần tử số nguyên `int` (4 bytes). Tránh khai báo mảng tĩnh quá lớn.

### 6. Ví dụ minh họa
**Bài toán:** Cho mảng $A$ có $N$ phần tử ($N \le 10^{18}$), tính số Fibonacci thứ $N$ theo modulo $10^9 + 7$.
- Phân tích Constraints: $N \le 10^{18}$ loại bỏ ngay lập tức vòng lặp $O(N)$.
- Thuật toán bắt buộc phải là $O(\log N)$.
- Hướng suy nghĩ: Tìm cấu trúc nhân ma trận:
$$\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix} \implies \begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$
- Sử dụng Binary Exponentiation trên ma trận $2 \times 2$ để đạt $O(8 \log N)$.

### 7. Những trường hợp dễ nhầm lẫn
- Bỏ qua hằng số ẩn (Hidden Constant $C$ trong $O(C \cdot N)$): Ví dụ một thuật toán $O(N \log N)$ nhưng thao tác với cấu trúc dữ liệu nặng (`std::map`, phép chia modulo liên tục) có thể chậm hơn một thuật toán $O(N)$ tối ưu cache tới 10-20 lần.
- Không để ý đến tổng $\sum N$ qua nhiều test case ($t \le 10^4, \sum N \le 2 \cdot 10^5$). Cần chú ý reset biến và mảng bằng cách chỉ dọn dẹp đúng những phần tử đã dùng thay vì `memset(a, 0, sizeof(a))` gây TLE $O(T \cdot \text{MAXN})$.

### 8. Bài tập vận dụng
- [CSES - Fibonacci Numbers](https://cses.fi/problemset/task/1722) (Độ khó: 1300 - $N \le 10^{18}$, áp dụng Matrix Exponentiation).
- [Codeforces 1201C - Maximum Median](https://codeforces.com/problemset/problem/1201/C) (Rating: 1400 - $N \le 2 \cdot 10^5, K \le 10^9$, định hướng Chặt nhị phân kết quả).

---

## 1.3. Pattern Recognition (Tư duy Nhận diện Khuôn mẫu)

### 1. Định nghĩa
Pattern Recognition là khả năng ánh xạ các đặc trưng trừu tượng của đề bài về các mô hình bài toán trừu tượng kinh điển đã được nghiên cứu và hiểu rõ.

### 2. Bản chất
Đề bài CP luôn được bao bọc bởi một lớp vỏ ngữ cảnh (câu chuyện thực tế về game, mạng lưới giao thông, mua bán cổ phiếu...). Bản chất của việc nhận diện khuôn mẫu là "lột bỏ" lớp vỏ ngữ cảnh để tìm ra hạt nhân cấu trúc dữ liệu và quan hệ giữa các đối tượng.

### 3. Khi nào sử dụng?
Áp dụng sau bước Brute Force và phân tích Constraints, khi tìm kiếm các mối quan hệ cấu trúc giữa các phần tử trong đề bài.

### 4. Dấu hiệu nhận biết
- "Tìm giá trị nhỏ nhất của giá trị lớn nhất..." $\to$ Chặt nhị phân trên tập kết quả (Binary Search on Answer).
- "Đoạn con liên tiếp thỏa mãn điều kiện có tính chất bao hàm..." $\to$ Two Pointers / Sliding Window.
- "Truy vấn trên đoạn của mảng tĩnh, không có cập nhật..." $\to$ Sparse Table / Prefix Sums / Disjoint Sparse Table.
- "Các sự kiện diễn ra theo thời gian hoặc tọa độ tăng dần..." $\to$ Sweep Line.
- "Tìm đường đi ngắn nhất trên đồ thị có trọng số 0 hoặc 1..." $\to$ 0-1 BFS với `std::deque`.

### 5. Quy trình suy luận
1. Viết lại yêu cầu bài toán dưới dạng ngôn ngữ toán học thuần túy.
2. Kiểm tra tính đơn điệu (Monotonicity): Nếu tăng biến $X$, kết quả $f(X)$ có luôn tăng hoặc luôn giảm không?
3. Kiểm tra tính chất con tối ưu (Optimal Substructure): Lời giải bài toán lớn có được ghép từ bài toán con độc lập không?
4. Khớp các tính chất với danh mục các bài toán chuẩn.

### 6. Ví dụ minh họa
**Bài toán:** Cho một dãy gồm $N$ công việc, mỗi công việc có thời gian bắt đầu $S_i$ và kết thúc $E_i$. Tìm số lượng công việc lớn nhất có thể chọn sao cho không có 2 công việc nào trùng thời gian.
- Nhận diện khuôn mẫu: Interval Scheduling Problem.
- Greedy Strategy: Luôn chọn công việc có thời gian kết thúc sớm nhất ($E_i$ nhỏ nhất) để để lại khoảng trống nhiều nhất cho các công việc phía sau.

### 7. Những trường hợp dễ nhầm lẫn
- Bị đánh lừa bởi từ khóa: Thấy từ "ngắn nhất" lập tức dùng BFS hoặc Dijkstra mà không nhận ra bài toán có thể là Quy hoạch động trên DAG hoặc bài toán tìm xâu con ngắn nhất.
- Áp dụng khuôn mẫu cứng nhắc khi bài toán có một điều kiện phụ (twist) làm phá vỡ tính chất cốt lõi của khuôn mẫu đó.

### 8. Bài tập vận dụng
- [CSES - Movie Festival](https://cses.fi/problemset/task/1629) (Độ khó: 1100 - Nhận diện Interval Scheduling).
- [CSES - Factory Machines](https://cses.fi/problemset/task/1620) (Độ khó: 1200 - Nhận diện Binary Search on Answer).

---

## 1.4. Mathematical Observation (Quan sát Bản chất Toán học)

### 1. Định nghĩa
Mathematical Observation là quá trình phân tích bài toán dưới góc nhìn lý thuyết số, tổ hợp, đại số hoặc hình học để phát hiện ra các quy luật tiềm ẩn, qua đó rút gọn bài toán phức tạp thành một công thức giải tích đóng hoặc một thuật toán cực kỳ đơn giản.

### 2. Bản chất
Nhiều bài toán trông có vẻ cần mô phỏng hàng triệu bước thực chất là một chu kỳ tuần hoàn (Cycle), một dãy số quy luật, hoặc một đẳng thức đại số có thể biến đổi triệt tiêu các thành phần phức tạp.

### 3. Khi nào sử dụng?
- Khi đề bài mô tả một quá trình lặp đi lặp lại với số bước cực lớn ($K \le 10^{18}$).
- Khi $N$ rất lớn nhưng không gian nghiệm lại rất nhỏ.
- Khi các phép toán liên quan đến XOR, AND, OR hoặc Modulo.

### 4. Dấu hiệu nhận biết
- Đề bài cho các thao tác biến đổi số học trên một tập hợp.
- Có sự xuất hiện của các yếu tố đối xứng hoặc triệt tiêu.
- Khi chạy thử bằng tay với các giá trị nhỏ ($N = 1, 2, 3, 4, 5, 6$) và ghi lại kết quả ra giấy, bạn thấy một chu kỳ hoặc một dãy số quen thuộc (Fibonacci, lũy thừa của 2, cấp số cộng).

### 5. Quy trình suy luận
1. **Lập bảng thực nghiệm (Experimentation Table):** Viết chương trình Brute Force đơn giản chạy thử với $N$ từ 1 đến 20.
2. **Quan sát đầu ra:** Tìm kiếm các đặc điểm: Số chẵn/lẻ? Có chu kỳ lặp lại không? Số lượng ước số?
3. **Phỏng đoán quy luật (Conjecture):** Đưa ra giả thuyết toán học (ví dụ: "Kết quả luôn bằng $2^N - 1$").
4. **Chứng minh sơ bộ:** Dùng quy nạp toán học hoặc nguyên lý bù trừ để giải thích vì sao quy luật đó lại xuất hiện.

### 6. Ví dụ minh họa
**Bài toán:** Có $N$ bóng đèn được đánh số từ $1$ đến $N$, ban đầu đều tắt. Có $N$ người lần lượt đi qua: người thứ $i$ sẽ đảo trạng thái của tất cả các bóng đèn có số thứ tự là bội của $i$. Hỏi sau khi $N$ người đi qua, có bao nhiêu bóng đèn đang sáng?
- Quan sát thực nghiệm:
  - Bóng $1$: chuyển ở lượt 1 $\to$ BẬT.
  - Bóng $2$: chuyển ở lượt 1, 2 $\to$ TẮT.
  - Bóng $3$: chuyển ở lượt 1, 3 $\to$ TẮT.
  - Bóng $4$: chuyển ở lượt 1, 2, 4 $\to$ BẬT.
  - Bóng $9$: chuyển ở lượt 1, 3, 9 $\to$ BẬT.
- Bản chất toán học: Bóng thứ $K$ được đảo trạng thái đúng bằng số lượng ước số của $K$. Một số có số lượng ước số là số lẻ khi và chỉ khi nó là **số chính phương** (vì các ước số thường đi theo cặp $(d, K/d)$, chỉ có ước căn bậc hai $\sqrt{K} = d$ là đứng một mình).
- Kết luận: Số bóng đèn sáng chính bằng số lượng số chính phương trong đoạn $[1, N]$, tức là $\lfloor \sqrt{N} \rfloor$.
- Thuật toán giải quyết trong $O(1)$: `return (long long)sqrt(n);` thay vì mô phỏng $O(N \log N)$!

### 7. Những trường hợp dễ nhầm lẫn
- Quy luật chỉ đúng với vài số đầu tiên nhưng gãy ở các số lớn hơn (hiện tượng Strong Law of Small Numbers). Luôn kiểm tra giả thuyết với ít nhất $N = 15$ đến $30$.

### 8. Bài tập vận dụng
- [Codeforces 230B - T-primes](https://codeforces.com/problemset/problem/230/B) (Rating: 1300 - Bản chất toán học về số có đúng 3 ước).
- [CSES - Common Divisors](https://cses.fi/problemset/task/1081) (Độ khó: 1400 - Đếm bội số để tìm GCD lớn nhất).

---

## 1.5. Invariant Thinking (Tư duy Bất biến)

### 1. Định nghĩa
Invariant (Bất biến) là một đại lượng, một tính chất hoặc một mối quan hệ không bao giờ thay đổi sau bất kỳ bước biến đổi hay thao tác hợp lệ nào của hệ thống.

### 2. Bản chất
Khi một bài toán cho phép thực hiện liên tiếp các thao tác và hỏi: "Có thể biến đổi trạng thái ban đầu thành trạng thái mục tiêu được hay không?", việc tìm ra một đại lượng bất biến sẽ chứng minh ngay lập tức trạng thái đích là bất khả thi nếu bất biến của nó khác với bất biến của trạng thái ban đầu.

### 3. Khi nào sử dụng?
- Các bài toán trò chơi (Game Theory), biến đổi lưới, đảo dấu các phần tử.
- Bài toán hỏi: "Is it possible to reach state B from state A?"

### 4. Dấu hiệu nhận biết
- Mỗi thao tác thay thế một cặp phần tử $(x, y)$ bằng $(x+1, y-1)$ $\to$ Tổng $\sum A_i$ là bất biến.
- Mỗi thao tác thay đổi trạng thái của 2 phần tử lân cận $\to$ Tính chẵn lẻ (Parity) của số lượng phần tử âm hoặc số nghịch thế (Inversion Count) là bất biến modulo 2.
- Phép toán XOR trên hai phần tử giống nhau: $x \oplus x = 0$.

### 5. Quy trình suy luận
1. Liệt kê các đại lượng có thể đo lường: Tổng các phần tử, Tổng modulo $K$, Tính chẵn lẻ, Số cặp nghịch thế, Tổng trọng số theo vị trí $\sum i \cdot A_i$.
2. Phân tích ảnh hưởng của một thao tác lên các đại lượng này.
3. Tìm đại lượng $I(S)$ sao cho nếu trạng thái $S \to S'$ thì $I(S) \equiv I(S') \pmod M$.
4. So sánh $I(S_{\text{start}})$ và $I(S_{\text{target}})$. Nếu $I(S_{\text{start}}) \ne I(S_{\text{target}})$, kết luận ngay là IMPOSSIBLE.

### 6. Ví dụ minh họa
**Bài toán:** Cho một mảng số nguyên. Mỗi bước cho phép chọn hai phần tử bất kỳ $A_i, A_j$ và trừ mỗi số đi $1$. Hỏi có thể làm cho toàn bộ mảng về 0 được không?
- Phân tích bất biến:
  - Mỗi bước, tổng $\sum A_k$ giảm đi đúng 2 đơn vị.
  - Do đó, tính chẵn lẻ của tổng mảng $\sum A_k \pmod 2$ không bao giờ đổi. Nếu ban đầu tổng là lẻ, không bao giờ đưa về 0 được!
  - Điều kiện cần thứ hai: Phần tử lớn nhất $\max(A) \le \sum A_k - \max(A)$ (nếu một số quá lớn, các số còn lại không đủ để triệt tiêu nó).
- Đây là lời giải hoàn chỉnh chỉ dựa trên 2 quan sát bất biến.

### 7. Những trường hợp dễ nhầm lẫn
- Bất biến chỉ cung cấp **điều kiện cần** (Necessary Condition), chưa chắc đã là **điều kiện đủ** (Sufficient Condition). Cần kiểm tra xem khi thỏa mãn bất biến thì có thể kiến tạo được cách biến đổi hay không.

### 8. Bài tập vận dụng
- [Codeforces 1365B - Trouble Sort](https://codeforces.com/problemset/problem/1365/B) (Rating: 1200 - Nhận diện bất biến về khả năng hoán đổi dựa trên loại phần tử).
- [CSES - Tower of Hanoi](https://cses.fi/problemset/task/2165) (Độ khó: 1000 - Bất biến về thứ tự đĩa).

---

## 1.6. Greedy Thinking (Tư duy Tham lam & Điều kiện Tối ưu địa phương)

### 1. Định nghĩa
Greedy Thinking là phương pháp giải quyết bài toán tối ưu bằng cách thực hiện một chuỗi các lựa chọn cục bộ tốt nhất tại từng bước (Locally Optimal Choice), với hy vọng rằng chuỗi lựa chọn đó sẽ dẫn đến nghiệm tối ưu toàn cục (Globally Optimal Solution).

### 2. Bản chất
Greedy hoạt động khi bài toán có hai tính chất nền tảng:
1. **Thuộc tính lựa chọn tham lam (Greedy Choice Property):** Nghiệm tối ưu toàn cục có thể được xây dựng bằng cách chọn lựa chọn tối ưu địa phương mà không cần phải xem xét lại quyết định trong quá khứ.
2. **Cấu trúc con tối ưu (Optimal Substructure):** Sau khi thực hiện một lựa chọn tham lam, bài toán thu gọn về một bài toán con cùng dạng với kích thước nhỏ hơn.

### 3. Khi nào sử dụng?
- Khi bài toán yêu cầu tìm cấu hình lớn nhất, nhỏ nhất, ít bước nhất.
- Khi không gian bài toán quá lớn để dùng DP hoặc Brute Force, nhưng các phần tử có thể sắp xếp theo một tiêu chí rõ ràng.

### 4. Dấu hiệu nhận biết
- Các phần tử có thể được sắp xếp theo một thứ tự tự nhiên (tăng dần giá trị, giảm dần thời gian, tỉ số giá trị/trọng lượng).
- Không có sự đánh đổi (Trade-off) phức tạp: Việc chọn phần tử tốt nhất bây giờ không làm mất đi các cơ hội tốt hơn trong tương lai.

### 5. Quy trình suy luận
1. Đề xuất tiêu chuẩn tham lam: Nên ưu tiên đại lượng nào trước? (Ví dụ: Ưu tiên việc ngắn nhất, ưu tiên phần tử lớn nhất...).
2. Thử tìm phản ví dụ (Counterexample hunting): Tự chế ra 3-5 test case nhỏ cố gắng "đánh lừa" tiêu chí tham lam.
3. Nếu không tìm được phản ví dụ, tiến hành chứng minh bằng **Kỹ thuật Đổi chỗ (Exchange Argument)**:
   - Giả sử tồn tại một lời giải tối ưu $OPT$ khác với lời giải tham lam $ALG$.
   - Tìm vị trí đầu tiên mà $OPT$ khác $ALG$.
   - Thực hiện thao tác hoán vị/đổi chỗ phần tử của $OPT$ để biến nó dần về $ALG$ mà chất lượng nghiệm không bị giảm sút.
   - Kết luận $ALG$ cũng là tối ưu.

### 6. Ví dụ minh họa
**Bài toán Fractional Knapsack:** Có $N$ món hàng, mỗi món có trọng lượng $W_i$ và giá trị $V_i$. Balo có sức chứa $C$. Được phép lấy một phần phân số của món hàng.
- Tiêu chí tham lam: Sắp xếp các món hàng theo tỉ số đơn giá giảm dần: $\frac{V_i}{W_i}$.
- Lần lượt lấy tối đa món hàng có tỉ số cao nhất cho đến khi đầy balo.

### 7. Những trường hợp dễ nhầm lẫn
- Áp dụng Greedy cho bài toán 0/1 Knapsack (nơi không được chia nhỏ món hàng): Khi đó Greedy theo đơn giá sẽ thất bại hoàn toàn. 0/1 Knapsack bắt buộc phải dùng Dynamic Programming.
- Nhầm lẫn giữa trực giác thông thường và tính đúng đắn toán học: 90% lỗi Wrong Answer trong CP đến từ việc "cảm thấy Greedy có vẻ đúng" mà không qua bước chứng minh hoặc tìm phản ví dụ.

### 8. Bài tập vận dụng
- [CSES - Tasks and Deadlines](https://cses.fi/problemset/task/1630) (Độ khó: 1200 - Chứng minh Greedy bằng Exchange Argument).
- [CSES - Ferris Wheel](https://cses.fi/problemset/task/1090) (Độ khó: 1000 - Ghép cặp lớn nhất với nhỏ nhất).

---

## 1.7. Divide and Conquer (Tư duy Chia để trị)

### 1. Định nghĩa
Divide and Conquer là phương pháp chia bài toán ban đầu thành hai hoặc nhiều bài toán con độc lập có kích thước nhỏ hơn cùng dạng, giải quyết các bài toán con đó một cách đệ quy, rồi kết hợp (Combine) kết quả của chúng để thu được lời giải cho bài toán ban đầu.

### 2. Bản chất
Giảm độ phức tạp tính toán thông qua cấu trúc cây đệ quy: Nếu việc chia đôi bài toán kích thước $N$ thành 2 bài toán kích thước $N/2$ và việc gộp kết quả mất thời gian $O(N)$, theo Định lý Thợ (Master Theorem): $T(N) = 2T(N/2) + O(N) \implies T(N) = O(N \log N)$.

### 3. Khi nào sử dụng?
- Khi bài toán trên một dãy có thể chia thành hai nửa độc lập: Trái và Phải.
- Khi một đối tượng thỏa mãn điều kiện nằm hoàn toàn ở nửa Trái, hoàn toàn ở nửa Phải, hoặc **băng qua điểm chia giữa** (Crossing the midpoint).

### 4. Dấu hiệu nhận biết
- Đề bài yêu cầu đếm số cặp nghịch thế, tìm cặp điểm gần nhất, nhân đa thức, hoặc tính lũy thừa lớn.

### 5. Quy trình suy luận
1. **Divide:** Chia dãy $A[L..R]$ tại điểm $M = (L + R) / 2$.
2. **Conquer:** Đệ quy giải trên đoạn trái $[L..M]$ và đoạn phải $[M+1..R]$.
3. **Combine (Bước mấu chốt):** Tính toán các đóng góp hoặc tương tác liên quan đến cả hai nửa (một phần tử nằm bên trái, một phần tử nằm bên phải). Thiết kế bước này sao cho thời gian chạy tuyến tính hoặc $O(K \log K)$.

### 6. Ví dụ minh họa
**Bài toán Đếm cặp nghịch thế (Inversion Counting):** Cho mảng $A$, đếm số cặp $(i, j)$ sao cho $i < j$ và $A[i] > A[j]$.
- Bản chất: Áp dụng Merge Sort.
- Khi trộn hai mảng đã sắp xếp $Left$ và $Right$, nếu phần tử $Left[p] > Right[q]$, thì mọi phần tử từ $p$ đến cuối của mảng $Left$ đều lớn hơn $Right[q]$. Ta cộng dồn ngay được $(M - p + 1)$ cặp mà không cần duyệt từng phần tử.

### 7. Những trường hợp dễ nhầm lẫn
- Nhầm lẫn giữa Divide and Conquer và Dynamic Programming: Divide and Conquer áp dụng khi các bài toán con **hoàn toàn độc lập** (không gối lên nhau - non-overlapping subproblems). Nếu các bài toán con lặp lại nhiều lần, phải dùng DP để lưu vết tránh tính lại.

### 8. Bài tập vận dụng
- [VNOI - NKINV](https://oj.vnoi.info/problem/nkinv) (Độ khó: 1300 - Đếm số cặp nghịch thế).
- [Codeforces 1042D - Petya and Array](https://codeforces.com/problemset/problem/1042/D) (Rating: 1800 - Chia để trị đếm số đoạn con có tổng nhỏ hơn $T$).

---

## 1.8. Reverse Thinking (Tư duy Đảo ngược bài toán)

### 1. Định nghĩa
Reverse Thinking là chiến lược tiếp cận bài toán từ trạng thái kết thúc (Target) đi ngược về trạng thái bắt đầu (Source), hoặc tính toán phần bù: Thay vì đếm trực tiếp số đối tượng thỏa mãn điều kiện khó, ta đếm toàn bộ rồi trừ đi số đối tượng không thỏa mãn.

### 2. Bản chất
- Trong nhiều quá trình vật lý hoặc đồ thị, thao tác xuôi làm gia tăng độ phức tạp (ví dụ: phá hủy liên kết, xóa đỉnh), nhưng thao tác ngược lại chính là quá trình xây dựng (thêm cạnh, kết nối thành phần), cho phép tận dụng các cấu trúc dữ liệu như Disjoint Set Union (DSU).
- Về mặt đếm: $|A| = |U| - |A^c|$ (Nguyên lý Phần bù).

### 3. Khi nào sử dụng?
- Đề bài có thao tác: Xóa đỉnh, phá hủy cạnh, rút bớt phần tử.
- Đề bài yêu cầu: "Tính số lượng cấu hình thỏa mãn ÍT NHẤT một tính chất..." $\to$ Nghĩ ngay đến tính phần bù: "Không thỏa mãn tính chất nào".
- Bài toán tìm đường đi mà đích đến cố định nhưng có nhiều điểm xuất phát.

### 4. Dấu hiệu nhận biết
- Từ khóa: "Xóa dần các cạnh cho đến khi...", "Tại mỗi bước loại bỏ một số...", "Đếm số dãy có ít nhất một số chia hết cho...".

### 5. Quy trình suy luận
1. **Kiểm tra tính khả nghịch:** Thao tác xuôi từ $A \to B$ có thể đảo thành thao tác ngược từ $B \to A$ hay không?
2. **Lưu vết truy vấn (Offline Queries):** Đọc toàn bộ các truy vấn xóa vào một danh sách.
3. **Thực hiện từ dưới lên:** Bắt đầu từ trạng thái cuối cùng (khi tất cả các thao tác xóa đã hoàn tất).
4. **Đảo xóa thành thêm:** Lần lượt thêm các cạnh/phần tử ngược từ truy vấn cuối cùng về truy vấn đầu tiên, dùng DSU để cập nhật thông tin trong $O(\alpha(N))$.
5. Đảo ngược mảng kết quả trước khi in ra.

### 6. Ví dụ minh họa
**Bài toán:** Cho đồ thị $N$ đỉnh ban đầu có $M$ cạnh. Người ta lần lượt xóa đi từng cạnh một cho đến hết. Sau mỗi lần xóa, hỏi đồ thị còn bao nhiêu thành phần liên thông?
- Hướng xuôi: Xóa cạnh trên đồ thị rất khó cập nhật thành phần liên thông nếu không dùng Dynamic Graph Connectivity phức tạp ($O(\log^2 N)$).
- Hướng ngược: Bắt đầu từ đồ thị rỗng (sau khi đã xóa hết). Đọc ngược các cạnh bị xóa từ dưới lên và thêm dần vào bằng DSU! Mỗi lần thêm một cạnh, nếu 2 đỉnh chưa cùng thành phần liên thông, số lượng thành phần giảm đi 1. Thuật toán đạt $O(M \alpha(N))$.

### 7. Những trường hợp dễ nhầm lẫn
- Quên đảo ngược thứ tự các truy vấn hoặc quên in ngược mảng kết quả cuối cùng.
- Không nhận diện được thao tác đảo ngược có tạo ra tính chất dễ hơn hay không.

### 8. Bài tập vận dụng
- [Codeforces 295B - Greg and Graph](https://codeforces.com/problemset/problem/295/B) (Rating: 1700 - Đảo ngược thứ tự xóa đỉnh trong Floyd-Warshall thành thêm đỉnh).
- [CSES - Counting Divisors](https://cses.fi/problemset/task/1713) (Độ khó: 1200 - Tư duy ngược: Thay vì tìm ước của từng số, đi rải bội số).

---

## 1.9. Constructive Thinking (Tư duy Kiến tạo nghiệm)

### 1. Định nghĩa
Constructive Thinking là tư duy giải quyết các bài toán yêu cầu xây dựng một cấu hình cụ thể (mảng, ma trận, đồ thị, chuỗi thao tác) thỏa mãn một tập hợp các ràng buộc nghiêm ngặt, mà không có sẵn một công thức tổng quát hay thuật toán mẫu.

### 2. Bản chất
Không phải là tìm kiếm hay duyệt, mà là **phát minh ra một quy luật xây dựng có hệ thống** (Systematic Rule) sao cho mọi ràng buộc tự động được thỏa mãn bằng cấu trúc do ta tạo ra.

### 3. Khi nào sử dụng?
- Đề bài bắt đầu bằng: "Construct an array...", "Find ANY valid configuration...", "Print a matrix such that...".
- Không yêu cầu tối ưu hóa hàm mục tiêu, chỉ yêu cầu tìm MỘT cấu hình hợp lệ.

### 4. Dấu hiệu nhận biết
- Đi kèm với câu: "If there are multiple answers, output any of them. If impossible, output -1."
- Thường xuất hiện ở bài B, C, D của các kỳ thi Codeforces Div 2.

### 5. Quy trình suy luận
1. **Thử nghiệm kích thước nhỏ:** Giải bằng tay cho $N = 1, 2, 3, 4, 5$.
2. **Khám phá các điểm cực trị (Extreme Cases):** Thử điền toàn số lớn nhất, toàn số 0, hoặc xen kẽ $0, 1, 0, 1$.
3. **Chia bài toán thành các khối đối xứng hoặc khối độc lập:** Xây dựng cho $N$ nhỏ, rồi tìm cách nhân bản hoặc mở rộng cấu trúc từ $N$ lên $N+2$ hoặc $2N$.
4. **Kiểm tra tính chẵn lẻ / Định lý Dirichlet:** Xác định điều kiện khi nào thì bài toán chắc chắn vô nghiệm (để in -1).

### 6. Ví dụ minh họa
**Bài toán:** Cho số nguyên $N$. Hãy dựng một hoán vị của các số từ $1$ đến $N$ sao cho tổng của hai phần tử liên tiếp bất kỳ không phải là số nguyên tố, hoặc in -1 nếu không thể.
- Phân tích kiến tạo: Ta biết tổng của hai số cùng tính chẵn lẻ luôn là số chẵn (hợp số nếu $> 2$).
- Quy luật kiến tạo: Gom toàn bộ các số lẻ sang một bên, toàn bộ các số chẵn sang một bên!
  - Dãy lẻ: $1, 3, 5, 7, \dots$ (tổng 2 số liên tiếp luôn chẵn $\ge 4$).
  - Dãy chẵn: $2, 4, 6, 8, \dots$ (tổng 2 số liên tiếp luôn chẵn $\ge 6$).
  - Nút thắt: Điểm nối giữa số lẻ cuối cùng và số chẵn đầu tiên. Ta chỉ cần chọn số lẻ cuối cùng và số chẵn đầu tiên sao cho tổng của chúng là hợp số (ví dụ chọn cặp tổng bằng 9 hoặc nối khéo léo).

### 7. Những trường hợp dễ nhầm lẫn
- Cố gắng tìm thuật toán tổng quát bằng DP/Đồ thị cho một bài toán thuần tính kiến tạo. Điều này dẫn đến code cực dài và quá thời gian.
- Bỏ quên trường hợp $N$ nhỏ đặc biệt (Corner Cases: $N=1, 2, 3$) mà quy luật kiến tạo chưa hoạt động đúng.

### 8. Bài tập vận dụng
- [Codeforces 1352G - Special Permutation](https://codeforces.com/problemset/problem/1352/G) (Rating: 1600 - Kiến tạo hoán vị với hiệu lân cận từ 2 đến 4).
- [Codeforces 1475D - Cleaning the Phone](https://codeforces.com/problemset/problem/1475/D) (Rating: 1800 - Kiến tạo kết hợp tham lam).

---

## 1.10. Reduction Thinking (Tư duy Quy nạp & Thu gọn bài toán)

### 1. Định nghĩa
Reduction Thinking (Tư duy Quy giảm) là quá trình biến đổi một bài toán mới lạ $P$ về một bài toán quen thuộc $Q$ đã có thuật toán chuẩn hóa, sao cho lời giải của $Q$ có thể chuyển hóa trực tiếp thành lời giải của $P$.

### 2. Bản chất
"Đứng trên vai người khổng lồ". Không phát minh lại bánh xe. Nhận diện các mối tương đương toán học để quy bài toán về: Bipartite Matching, Max Flow, Shortest Path, 2-SAT, hoặc Dynamic Programming.

### 3. Khi nào sử dụng?
Khi bài toán có những ràng buộc phức tạp giữa các cặp đối tượng và có cảm giác rất giống một mô hình đồ thị kinh điển nhưng chưa rõ cách nối cạnh.

### 4. Dấu hiệu nhận biết
- Lựa chọn nhị phân thỏa mãn điều kiện logic dạng: "(Nếu chọn $A$ thì phải chọn $B$) VÀ (Không được chọn cả $C$ và $D$)" $\to$ **Quy về 2-SAT**.
- Phân chia các đối tượng vào 2 nhóm sao cho chi phí tối đa/tối thiểu $\to$ **Quy về Min Cut (Định lý Cắt hẹp nhất - Luồng cực đại)**.
- Bài toán tìm chuỗi thao tác ít nhất trên lưới $\to$ **Quy về BFS trên đồ thị trạng thái**.

### 5. Quy trình suy luận
1. Liệt kê các bài toán chuẩn có tính chất tương tự.
2. Thiết lập ánh xạ (Mapping):
   - Đối tượng trong đề $\leftrightarrow$ Đỉnh trong đồ thị.
   - Ràng buộc/Chi phí $\leftrightarrow$ Trọng số cạnh hoặc Dung lượng cạnh (Capacity).
3. Chứng minh tính tương đương: Lời giải hợp lệ bên bài toán $P$ tương ứng 1-1 với một lát cắt/luồng hợp lệ bên bài toán $Q$.

### 6. Ví dụ minh họa
**Bài toán Project Selection:** Có $N$ dự án mang lại lợi nhuận $P_i$. Để làm dự án $i$, bạn bắt buộc phải mua một số máy móc trong tập $M$. Mỗi máy móc có chi phí $C_j$. Một máy móc mua một lần có thể dùng cho nhiều dự án. Tìm lợi nhuận ròng lớn nhất.
- Quy giảm: Đây là bài toán kinh điển quy về **Min Cut (Lát cắt nhỏ nhất)** trên mạng luồng.
  - Nối đỉnh nguồn $S$ đến dự án $i$ với trọng số $P_i$ (nếu $P_i > 0$).
  - Nối dự án $i$ đến các máy móc cần thiết với trọng số $\infty$.
  - Nối máy móc $j$ đến đỉnh đích $T$ với trọng số là chi phí $C_j$.
  - Lợi nhuận cực đại = (Tổng lợi nhuận dương) - MinCut.

### 7. Những trường hợp dễ nhầm lẫn
- Quy giảm sai hướng: Cố quy một bài toán NP-Hard về một bài toán đa thức (ví dụ quy về Max Flow nhưng không xử lý được ràng buộc phi tuyến tính).

### 8. Bài tập vận dụng
- [CSES - Distinct Routes](https://cses.fi/problemset/task/1711) (Độ khó: 1700 - Quy giảm bài toán tìm đường đi không giao nhau về Max Flow).
- [CSES - Giant Pizza](https://cses.fi/problemset/task/1684) (Độ khó: 1600 - Quy giảm bài toán chọn topping pizza về 2-SAT).

---

## 1.11. State Modeling (Tư duy Mô hình hóa Trạng thái)

### 1. Định nghĩa
State Modeling là kỹ năng trừu tượng hóa toàn bộ thông tin cần thiết của một hệ thống tại một thời điểm thành một bộ tham số tối thiểu (Tuple/Vector), sao cho tương lai của hệ thống hoàn toàn độc lập với quá khứ một khi trạng thái hiện tại đã được xác định (Tính chất Markov).

### 2. Bản chất
Đây là xương sống của mọi thuật toán Dynamic Programming và BFS đồ thị trạng thái. Một mô hình trạng thái tốt phải đảm bảo 2 yếu tố:
1. **Đầy đủ (Sufficiency):** Chứa đủ thông tin để đưa ra quyết định chuyển tiếp cho các bước tiếp theo.
2. **Cực tiểu (Minimality):** Chứa ít chiều và miền giá trị nhỏ nhất có thể để tránh bùng nổ không gian trạng thái (State Space Explosion).

### 3. Khi nào sử dụng?
- Bất cứ khi nào thiết kế thuật toán Dynamic Programming.
- Khi giải các bài toán mô phỏng trò chơi, xúc xắc, di chuyển trên lưới với điều kiện phụ (chìa khóa, năng lượng, số lần quay xe).

### 4. Dấu hiệu nhận biết
- "Tại mỗi bước ta có thể thực hiện một trong các hành động...", kết quả phụ thuộc vào các quyết định trước đó nhưng chỉ cần nhớ thông tin tóm tắt (ví dụ: đã nhặt được bao nhiêu chìa khóa).

### 5. Quy trình suy luận
1. **Đặt câu hỏi:** "Để quyết định bước đi tiếp theo, tôi thực sự cần biết những gì về quá khứ?"
   - Có cần nhớ cả con đường đã đi qua không? (Nếu không, bỏ qua vết).
   - Chỉ cần nhớ đỉnh hiện tại? Thêm một số nguyên biểu diễn năng lượng còn lại?
2. **Khai báo Tuple trạng thái:** $State = (u, \text{mask}, \text{rem})$.
3. **Tính kích thước không gian trạng thái:** Nhân kích thước các chiều lại: $|S| = |U| \times 2^K \times M$.
4. Đối chiếu kích thước $|S|$ với giới hạn bộ nhớ (Memory Limit) và thời gian thực thi.

### 6. Ví dụ minh họa
**Bài toán:** Tìm đường đi ngắn nhất trên mê cung $N \times M$, trong đó có $K$ cánh cửa ($K \le 10$) và $K$ chìa khóa tương ứng nằm rải rác.
- Mô hình trạng thái ngây thơ: Lưu lại toàn bộ các ô đã đi qua $\to$ Không gian trạng thái khổng lồ, vô tận.
- Mô hình trạng thái tối ưu: $State(r, c, mask)$ trong đó:
  - $r, c$: Tọa độ hiện tại của nhân vật ($1 \le r \le N, 1 \le c \le M$).
  - $mask$: Mặt nạ bit độ dài $K$, bit thứ $i = 1$ nếu đã nhặt chìa khóa thứ $i$.
- Tổng số trạng thái: $N \times M \times 2^K$. Với $N, M \le 50, K \le 10 \implies 50 \times 50 \times 1024 \approx 2.5 \cdot 10^6$ trạng thái. Chạy BFS tìm đường đi ngắn nhất hoàn toàn khả thi trong 0.2s!

### 7. Những trường hợp dễ nhầm lẫn
- Thừa thông tin trong trạng thái: Đưa những biến không ảnh hưởng đến quyết định tương lai vào trạng thái làm bộ nhớ vượt quá giới hạn (MLE).
- Thiếu thông tin: Bỏ quên một ràng buộc dẫn đến vi phạm tính chất con tối ưu của DP (nghiệm con tính sai vì không biết trạng thái trước đó có vi phạm ràng buộc ẩn hay không).

### 8. Bài tập vận dụng
- [CSES - Elevator Rides](https://cses.fi/problemset/task/1653) (Độ khó: 1600 - Mô hình hóa trạng thái $dp(mask) = \{\text{số chuyến}, \text{trọng lượng thừa}\}$).
- [Codeforces 839C - Journey](https://codeforces.com/problemset/problem/839/C) (Rating: 1500 - Trạng thái đệ quy tính kỳ vọng trên cây).

---

## 1.12. Graph Modeling (Tư duy Đồ thị hóa bài toán thực tế)

### 1. Định nghĩa
Graph Modeling là khả năng biến đổi các đối tượng và quan hệ trong một bài toán tưởng chừng không liên quan đến đồ thị thành Đỉnh (Vertices) và Cạnh (Edges), từ đó kích hoạt sức mạnh của toàn bộ lý thuyết đồ thị phong phú (Shortest Path, MST, SCC, Max Flow).

### 2. Bản chất
Đồ thị là công cụ mạnh mẽ nhất để biểu diễn quan hệ nhị phân (Binary Relation) giữa các thực thể:
- Quan hệ phụ thuộc (Prerequisite) $\to$ Đồ thị có hướng $\to$ Topological Sort.
- Quan hệ xung đột (Conflict) $\to$ Đồ thị vô hướng $\to$ Graph Coloring / Independent Set.
- Quan hệ chuyển trạng thái có chi phí $\to$ Đồ thị có trọng số $\to$ Dijkstra / Bellman-Ford.

### 3. Khi nào sử dụng?
- Các bài toán về chuyển đổi từ (Word Ladder), hoán đổi vị trí quân cờ.
- Hệ thống luật lệ có điều kiện: "Để làm việc A cần hoàn thành việc B".
- Bài toán tìm chuỗi biến đổi ít bước nhất.

### 4. Dấu hiệu nhận biết
- Đề bài không hề nhắc đến từ "đồ thị", "cây" hay "đỉnh", nhưng có mô tả các phép biến đổi từ một đối tượng $X$ sang đối tượng $Y$ với chi phí nhất định.

### 5. Quy trình suy luận
1. **Định nghĩa Đỉnh (Vertex):** Mỗi cấu hình hoặc thực thể độc lập là một đỉnh.
2. **Định nghĩa Cạnh (Edge):** Có cạnh nối từ $u \to v$ nếu và chỉ nếu có một thao tác hợp lệ biến $u$ thành $v$.
3. **Gán trọng số cạnh (Weight):**
   - Trọng số = 1 (hoặc không trọng số): Mỗi thao tác tốn 1 bước $\to$ BFS.
   - Trọng số $\in \{0, 1\}$: Có thao tác miễn phí và thao tác tốn phí $\to$ 0-1 BFS.
   - Trọng số không âm bất kỳ: Chi phí tùy biến $\to$ Dijkstra.
4. **Xác định loại bài toán:** Tìm đường đi ngắn nhất? Tìm chu trình? Kiểm tra tính liên thông?

### 6. Ví dụ minh họa
**Bài toán:** Cho hai số nguyên $A$ và $B$. Mỗi bước bạn có thể nhân đôi số hiện tại ($x \to 2x$) hoặc trừ đi 1 ($x \to x - 1$). Tìm số bước ít nhất để biến $A$ thành $B$.
- Đồ thị hóa:
  - Đỉnh: Các số nguyên từ $1$ đến $\max(A, B) \times 2$.
  - Cạnh: Từ đỉnh $x$ có 2 cạnh có hướng đi ra:
    - Đến $2x$ với trọng số 1.
    - Đến $x - 1$ với trọng số 1.
  - Bài toán quy về: Tìm đường đi ngắn nhất từ đỉnh $A$ đến đỉnh $B$ trên đồ thị vô hướng không trọng số $\to$ Dùng BFS!

### 7. Những trường hợp dễ nhầm lẫn
- Số lượng đỉnh hoặc số lượng cạnh tiềm năng quá lớn (ví dụ đồ thị đầy đủ $N^2$ cạnh), dẫn đến TLE nếu dựng cạnh tường minh. Cần kỹ thuật **dựng cạnh ảo** (Virtual Nodes / Auxiliary Nodes) hoặc truy vấn cạnh ngầm định (Implicit Graph).

### 8. Bài tập vận dụng
- [Codeforces 510C - Fox and Names](https://codeforces.com/problemset/problem/510/C) (Rating: 1600 - Mô hình hóa thứ tự từ điển thành Đồ thị có hướng và tìm Topological Sort).
- [CSES - Message Route](https://cses.fi/problemset/task/1667) (Độ khó: 1000 - BFS cơ bản tìm đường đi ngắn nhất).

---

## 1.13. Optimization Thinking (Tư duy Tối ưu hóa tiệm tiến)

### 1. Định nghĩa
Optimization Thinking là quy trình nâng cấp tiệm tiến độ phức tạp của một giải pháp: Bắt đầu từ thuật toán ngây thơ (Brute Force), phân tích chính xác **nút thắt cổ chai** (Bottleneck) đang tiêu tốn nhiều thời gian nhất, sau đó thay thế nút thắt đó bằng một cấu trúc dữ liệu hoặc một tính chất toán học phù hợp.

### 2. Bản chất
Không cố gắng nhảy ngay vào thuật toán $O(N)$ hoàn hảo. Tư duy tối ưu hóa là một chuỗi biến đổi đại số hoặc cấu trúc:
$$O(N^3) \xrightarrow[\text{Khử vòng lặp}]{} O(N^2) \xrightarrow[\text{Cấu trúc dữ liệu}]{} O(N \log N) \xrightarrow[\text{Hai con trỏ/Monotonic}]{} O(N)$$

### 3. Khi nào sử dụng?
Khi bạn đã có trong tay thuật toán Brute Force hoặc thuật toán giải đúng nhưng bị quá thời gian (TLE).

### 4. Dấu hiệu nhận biết
- Trong code có hai hoặc ba vòng lặp lồng nhau (`for (int i...) for (int j...) for (int k...)`).
- Vòng lặp trong cùng thực hiện một tác vụ quen thuộc: "Tìm giá trị nhỏ nhất trong đoạn", "Tính tổng các phần tử", "Tìm phần tử đầu tiên lớn hơn $X$".

### 5. Quy trình suy luận
1. **Xác định Bottleneck:** Vòng lặp nào đang chiếm $O(N)$ thời gian? Nó đang làm gì?
2. **Khai thác tính chất tích lũy:**
   - Nếu nó tính tổng đoạn $\to$ Thay bằng **Prefix Sum** $O(1)$.
   - Nếu nó tìm min/max trên đoạn động $\to$ Thay bằng **Segment Tree** $O(\log N)$ hoặc **Sparse Table** $O(1)$.
   - Nếu phạm vi tìm kiếm dịch chuyển tịnh tiến $\to$ Thay bằng **Sliding Window với Monotonic Queue** $O(1)$ amortized.
   - Nếu hàm bên trong có tính đơn điệu $\to$ Thay vòng lặp duyệt tuyến tính bằng **Binary Search** $O(\log N)$.
3. **Tách rời các biến độc lập (Separation of Variables):** Biến đổi biểu thức $f(i, j) = A_i \cdot B_j + C_i - C_j$ thành các thành phần chỉ phụ thuộc vào $i$ và chỉ phụ thuộc vào $j$.

### 6. Ví dụ minh họa
**Bài toán:** Cho mảng $A$ gồm $N$ số. Tìm độ dài dãy con tăng dài nhất (LIS).
- Thuật toán 1 (Brute Force): Sinh toàn bộ $2^N$ dãy con, kiểm tra tính tăng $\to O(N \cdot 2^N)$.
- Thuật toán 2 (DP cơ bản): $dp[i]$ là độ dài LIS kết thúc tại $i$.
  $$dp[i] = 1 + \max_{j < i, A[j] < A[i]} dp[j]$$
  Hai vòng lặp lồng nhau $\to O(N^2)$. Nút thắt: Tìm $\max_{j < i, A[j] < A[i]} dp[j]$.
- Thuật toán 3 (Tối ưu bằng Fenwick Tree): Xem $A[j]$ là chỉ số, truy vấn max trên đoạn $[1, A[i]-1] \to O(N \log N)$.
- Thuật toán 4 (Patience Sorting): Duy trì mảng $tail[len]$ là giá trị kết thúc nhỏ nhất của dãy tăng độ dài $len$. Mảng $tail$ luôn tăng đơn điệu $\to$ Chặt nhị phân bằng `std::lower_bound` $\to O(N \log N)$ với hằng số cực nhỏ!

### 7. Những trường hợp dễ nhầm lẫn
- Tối ưu hóa vi mô (Micro-optimization): Cố gắng sửa `i++` thành `++i`, dùng bitwise thay phép chia, mở rộng vòng lặp mà không cải thiện độ phức tạp tiệm cận (Big-O). Thuật toán $O(N^2)$ dù tối ưu vi mô đến đâu cũng không thể chạy kịp với $N = 2 \cdot 10^5$.

### 8. Bài tập vận dụng
- [CSES - Increasing Subsequence](https://cses.fi/problemset/task/1145) (Độ khó: 1300 - Tối ưu LIS từ $O(N^2)$ về $O(N \log N)$).
- [Codeforces 459D - Pashmak and Parmida's problem](https://codeforces.com/problemset/problem/459/D) (Rating: 1800 - Tối ưu đếm cặp bằng Fenwick Tree).

---

## 1.14. Proof of Correctness (Tư duy Chứng minh tính đúng đắn)

### 1. Định nghĩa
Proof of Correctness là khả năng đưa ra lập luận logic chặt chẽ (toán học hoặc cấu trúc) để khẳng định thuật toán chắc chắn cho kết quả đúng trên **mọi test case có thể có**, đặc biệt là các trường hợp biên, trước khi gõ code.

### 2. Bản chất
Trong phòng thi, thời gian là tài sản quý nhất. Một lần nộp bài bị Wrong Answer (WA) không chỉ làm bạn mất 20 phút penalty mà còn phá hủy sự tự tin và gây hoang mang tâm lý. Khả năng chứng minh tính đúng đắn giúp bạn tự tin bấm nộp và chuyển sang bài tiếp theo.

### 3. Khi nào sử dụng?
- Bắt buộc phải thực hiện khi sử dụng thuật toán Tham lam (Greedy) hoặc Rút gọn trạng thái DP.
- Khi thiết kế điều kiện dừng của đệ quy và các bước cập nhật trong Chặt nhị phân.

### 4. Các phương pháp chứng minh kinh điển trong CP
1. **Quy nạp toán học (Mathematical Induction):**
   - Chứng minh đúng với trường hợp cơ sở ($N = 1$).
   - Giả sử đúng đến $N = k$, chứng minh thuật toán tiếp tục đúng với $N = k + 1$.
2. **Chứng minh bằng phản chứng (Proof by Contradiction):**
   - Giả sử thuật toán cho kết quả sai $\implies$ Dẫn tới một điều mâu thuẫn với giả thiết hoặc tính chất bài toán.
3. **Kỹ thuật đổi chỗ (Exchange Argument - cho Greedy):**
   - Chứng minh rằng bất kỳ lời giải tối ưu nào cũng có thể biến đổi dần về lời giải của thuật toán tham lam mà không làm giảm giá trị hàm mục tiêu.

### 5. Quy trình suy luận
1. Phát biểu rõ ràng thuật toán đề xuất: "Tôi sẽ chọn các phần tử theo thứ tự tiêu chí $C$".
2. Đặt giả thiết phản chứng: "Giả sử có một phương án $OPT$ khác biệt tại bước đầu tiên...".
3. Thực hiện hoán vị 2 phần tử kề nhau trong chuỗi quyết định của $OPT$.
4. So sánh hàm mục tiêu trước và sau khi hoán vị: Chứng minh $\Delta \ge 0$.
5. Kiểm tra các điều kiện biên: Tràn số (`long long`), chia cho 0, đồ thị không liên thông, mảng chỉ có 1 phần tử.

### 6. Ví dụ minh họa
**Bài toán:** Chứng minh thuật toán Kruskal tìm Cây khung nhỏ nhất (MST) luôn cho kết quả tối ưu.
- Lập luận bằng Cut Property (Tính chất lát cắt):
  - Giả sử cạnh $e = (u, v)$ có trọng số nhỏ nhất nối giữa hai tập đỉnh $S$ và $V \setminus S$.
  - Nếu một cây khung $T$ không chứa cạnh $e$, thì trong $T$ chắc chắn tồn tại một đường đi khác giữa $u$ và $v$, đường đi này phải băng qua lát cắt tại một cạnh $e' \ne e$.
  - Vì $e$ có trọng số nhỏ nhất qua lát cắt nên $w(e) \le w(e')$.
  - Thay thế $e'$ bằng $e$ trong $T$, ta thu được một cây khung mới $T' = T \cup \{e\} \setminus \{e'\}$ có tổng trọng số $w(T') = w(T) - w(e') + w(e) \le w(T)$.
  - Vậy cạnh nhỏ nhất luôn có thể thuộc về một cây khung nhỏ nhất.

### 7. Những trường hợp dễ nhầm lẫn
- "Proof by AC on Sample Tests": Kiểm tra thấy code chạy đúng với 3 ví dụ của đề bài rồi vội vã tin rằng thuật toán đúng. Sample tests thường được giám khảo thiết kế rất ngây thơ để bẫy các thuật toán tham lam sai!

### 8. Bài tập vận dụng
- [CSES - Road Reparation](https://cses.fi/problemset/task/1675) (Độ khó: 1200 - Bản chất và chứng minh thuật toán Kruskal / Prim).
- [Codeforces 1336A - Linova and Kingdom](https://codeforces.com/problemset/problem/1336/A) (Rating: 1600 - Chứng minh tiêu chí tham lam dựa trên độ sâu và kích thước cây con).

---


# CHƯƠNG 2: MATHEMATICAL THINKING

> *"Toán học không phải là công cụ phụ trợ cho thuật toán; toán học chính là hạt nhân cấu trúc của thuật toán."*

Trong các kỳ thi như ICPC hay kỳ thi Tin học Quốc gia, ít nhất 30% - 40% các bài toán trung bình đến khó đều có nền tảng lý thuyết số, đại số tổ hợp hoặc tính chất toán học ẩn giấu. Nếu không có tư duy toán học vững chắc, thí sinh sẽ bị mắc kẹt trong việc cố gắng áp dụng các cấu trúc dữ liệu phức tạp vào một bài toán thực chất chỉ cần một vài phép biến đổi đại số.

---

## 2.1. Number Theory (Số học chuyên sâu)

### 1. Ước chung lớn nhất (GCD) và Bội chung nhỏ nhất (LCM)
- **Thuật toán Euclid:** Dựa trên tính chất $\gcd(a, b) = \gcd(b, a \bmod b)$.
  - Độ phức tạp: $O(\log(\min(a, b)))$. Trường hợp xấu nhất xảy ra khi $a$ và $b$ là hai số Fibonacci liên tiếp.
- **Tính chất mở rộng cực kỳ quan trọng trong CP:**
  - $\gcd(a, b) \times \text{lcm}(a, b) = a \times b$.
  - $\gcd(a, b) = \gcd(a, b - a) = \gcd(a, a + b)$. Tính chất này cho phép tính GCD trên mảng hiệu (Difference Array) kết hợp Segment Tree để giải bài toán Range GCD Update.
  - $\gcd(a^m - 1, a^n - 1) = a^{\gcd(m, n)} - 1$.
  - Số lượng các giá trị GCD khác nhau của tất cả các tiền tố trong một mảng $N$ phần tử tối đa chỉ là $O(\log(\max A_i))$.

### 2. Số nguyên tố và Kỹ thuật Sàng (Sieve Techniques)
- **Kiểm tra nguyên tố căn bậc hai:** $O(\sqrt{N})$.
- **Sàng Eratosthenes chuẩn:** Tìm tất cả số nguyên tố $\le N$ trong $O(N \log \log N)$.
- **Sàng tuyến tính (Linear Sieve) và Ước nguyên tố nhỏ nhất (Smallest Prime Factor - SPF):**
  - Chạy đúng trong $O(N)$ bằng cách đảm bảo mỗi hợp số chỉ bị gạch bỏ đúng **duy nhất một lần** bởi ước nguyên tố nhỏ nhất của nó.
  - Giá trị SPF cho phép phân tích một số $X \le N$ ra thừa số nguyên tố trong thời gian $O(\log X)$.

```cpp
// Sàng tuyến tính tính SPF trong O(N)
const int MAXN = 1e7 + 5;
std::vector<int> primes;
int spf[MAXN];

void linearSieve() {
    for (int i = 2; i < MAXN; ++i) {
        if (spf[i] == 0) {
            spf[i] = i;
            primes.push_back(i);
        }
        for (int p : primes) {
            if (p > spf[i] || (long long)i * p >= MAXN) break;
            spf[i * p] = p;
        }
    }
}

// Phân tích thừa số nguyên tố O(log X)
std::vector<std::pair<int, int>> getFactorization(int x) {
    std::vector<std::pair<int, int>> factors;
    while (x > 1) {
        int p = spf[x];
        int count = 0;
        while (x % p == 0) {
            count++;
            x /= p;
        }
        factors.push_back({p, count});
    }
    return factors;
}
```

### 3. Số lượng ước số $d(n)$ và Tổng các ước số $\sigma(n)$
Nếu $N = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$:
- Số lượng ước số: $d(N) = \prod_{i=1}^k (a_i + 1)$.
  - Với $N \le 10^9$, $d(N) \le 1344$.
  - Với $N \le 10^{18}$, $d(N) \le 103680$.
- Tổng các ước số: $\sigma(N) = \prod_{i=1}^k \frac{p_i^{a_i + 1} - 1}{p_i - 1}$.

### 4. Đồng dư thức (Modular Arithmetic) & Lũy thừa nhị phân (Binary Exponentiation)
- Tính chất:
  $$(A + B) \bmod M = ((A \bmod M) + (B \bmod M)) \bmod M$$
  $$(A \times B) \bmod M = ((A \bmod M) \times (B \bmod M)) \bmod M$$
  $$(A - B) \bmod M = ((A \bmod M) - (B \bmod M) + M) \bmod M$$
- **Lũy thừa nhị phân tính $A^B \bmod M$ trong $O(\log B)$:**
```cpp
long long powerMod(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (__int128)res * base % mod;
        base = (__int128)base * base % mod;
        exp >>= 1;
    }
    return res;
}
```

### 5. Nghịch đảo Modulo (Modular Multiplicative Inverse)
- **Định lý Fermat nhỏ:** Nếu $M$ là số nguyên tố và $\gcd(A, M) = 1$, thì $A^{M-1} \equiv 1 \pmod M \implies A^{-1} \equiv A^{M-2} \pmod M$.
- **Thuật toán Euclid mở rộng (Extended Euclidean Algorithm):** Dùng khi $M$ không nhất thiết là số nguyên tố, chỉ cần $\gcd(A, M) = 1$. Tìm nghiệm nguyên $x, y$ của phương trình Diophantine: $Ax + My = 1 \implies Ax \equiv 1 \pmod M$.
```cpp
long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    long long x1, y1;
    long long d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

long long modInverse(long long a, long long m) {
    long long x, y;
    long long g = extgcd(a, m, x, y);
    if (g != 1) return -1; // Không tồn tại nghịch đảo
    return (x % m + m) % m;
}
```

---

## 2.2. Combinatorics (Tổ hợp & Đếm nâng cao)

### 1. Hoán vị, Chỉnh hợp và Tổ hợp
- Số hoán vị của $N$ phần tử: $P(N) = N!$.
- Tổ hợp chập $K$ của $N$:
  $$\binom{N}{K} = C_N^K = \frac{N!}{K!(N-K)!}$$
- **Tính toán nhanh trong modulo $P$ (với $P$ là số nguyên tố, thường là $10^9+7$ hoặc $998244353$):**
  Tiền xử lý giai thừa $fact[i]$ và nghịch đảo giai thừa $invFact[i]$ trong $O(N)$, sau đó mỗi truy vấn $\binom{N}{K}$ trả lời trong $O(1)$:
```cpp
const int MAX = 1e6 + 5;
const int MOD = 1e9 + 7;
long long fact[MAX], invFact[MAX];

void precomputeComb() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = fact[i - 1] * i % MOD;
    invFact[MAX - 1] = powerMod(fact[MAX - 1], MOD - 2, MOD);
    for (int i = MAX - 2; i >= 0; --i) invFact[i] = invFact[i + 1] * (i + 1) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}
```

### 2. Bài toán chia kẹo Euler (Stars and Bars)
- Số cách chia $N$ cái kẹo giống nhau cho $K$ đứa trẻ sao cho mỗi đứa có **ít nhất 1 cái**: $\binom{N-1}{K-1}$.
- Số cách chia $N$ cái kẹo giống nhau cho $K$ đứa trẻ sao cho mỗi đứa có thể **nhận 0 cái hoặc nhiều hơn**: $\binom{N+K-1}{K-1}$.

### 3. Số Catalan
Dãy số $C_n = \frac{1}{n+1}\binom{2n}{n} = \binom{2n}{n} - \binom{2n}{n-1}$.
Các mô hình tương đương kinh điển:
- Số dãy ngoặc đúng gồm $n$ cặp ngoặc mở và đóng.
- Số cách chia đa giác lồi $n+2$ đỉnh thành các tam giác bằng các đường chéo không cắt nhau.
- Số cây nhị phân đúng có $n$ nút trong.
- Số đường đi trên lưới từ $(0,0)$ đến $(n,n)$ không bao giờ vượt lên phía trên đường chéo chính $y = x$.

### 4. Định lý Lucas (Khi $N, K$ cực lớn nhưng Modulo $P$ là số nguyên tố nhỏ)
$$\binom{N}{K} \equiv \prod_{i=0}^m \binom{n_i}{k_i} \pmod P$$
Trong đó $n_i, k_i$ là các chữ số trong biểu diễn cơ số $P$ của $N$ và $K$. Cho phép tính $\binom{N}{K} \pmod P$ với $N, K \le 10^{18}, P \le 10^5$ trong thời gian $O(P + \log_P N)$.

---

## 2.3. Principles: Pigeonhole, PIE & Induction

### 1. Nguyên lý Dirichlet (Pigeonhole Principle)
- **Nội dung:** Nếu xếp nhiều hơn $N$ chú chim bồ câu vào $N$ cái chuồng, thì chắc chắn có ít nhất một cái chuồng chứa từ 2 chú chim trở lên.
- **Ứng dụng trong CP:**
  - **Tìm chu trình trong trạng thái hữu hạn:** Nếu một hệ thống có $K$ trạng thái có thể có, sau tối đa $K+1$ bước biến đổi chắc chắn sẽ lặp lại một trạng thái cũ (tạo thành chu kỳ).
  - **Tìm dãy con có tổng chia hết cho $N$:** Xét $N$ tổng tiền tố $S_1, S_2, \dots, S_N$. Vì chỉ có $N$ số dư khả dĩ modulo $N$, nếu có $S_i \equiv 0 \pmod N$ thì xong; nếu không, theo Dirichlet chắc chắn có 2 tổng $S_j \equiv S_i \pmod N \implies (S_j - S_i) \ \vdots \ N$.

### 2. Nguyên lý Bù trừ (Principle of Inclusion-Exclusion - PIE)
- Cho $n$ tập hợp $A_1, A_2, \dots, A_n$:
  $$\left| \bigcup_{i=1}^n A_i \right| = \sum_{i} |A_i| - \sum_{i < j} |A_i \cap A_j| + \sum_{i < j < k} |A_i \cap A_j \cap A_k| - \dots + (-1)^{n-1} \left| \bigcap_{i=1}^n A_i \right|$$
- **Ứng dụng:**
  - Đếm số số trong đoạn $[1, X]$ nguyên tố cùng nhau với $N$ (hoặc không chia hết cho các ước nguyên tố của $N$).
  - Bài toán số xáo trộn (Derangements - số hoán vị không có điểm cố định $D_n = n! \sum_{i=0}^n \frac{(-1)^i}{i!}$).

---

## 2.4. Probability & Expected Value (Xác suất & Kỳ vọng)

### 1. Tính tuyến tính của Kỳ vọng (Linearity of Expectation)
Đây là công cụ **mạnh mẽ nhất** để giải các bài toán kỳ vọng trong CP:
$$E[X_1 + X_2 + \dots + X_n] = E[X_1] + E[X_2] + \dots + E[X_n]$$
**ĐẶC BIỆT LƯU Ý:** Đẳng thức này luôn đúng mà **KHÔNG CẦN CÁC BIẾN NGẪU NHIÊN ĐỘC LẬP VỚI NHAU**.

### 2. Kỹ thuật Biến chỉ thị (Indicator Random Variable)
- Đặt biến ngẫu nhiên $I_k = 1$ nếu biến cố $k$ xảy ra, và $I_k = 0$ nếu không xảy ra.
- Khi đó $E[I_k] = 1 \times P(\text{Biến cố } k) + 0 \times P(\dots) = P(\text{Biến cố } k)$.
- Kỳ vọng của tổng số biến cố xảy ra: $E[\text{Total}] = \sum E[I_k] = \sum P(\text{Biến cố } k)$.

### 3. Quy hoạch động tính Kỳ vọng (Expected Value DP)
- Định nghĩa $E[u]$ là kỳ vọng chi phí để đi từ trạng thái $u$ đến trạng thái đích.
  $$E[u] = \sum_{v} P(u \to v) \times (E[v] + W(u \to v))$$
- Nếu đồ thị trạng thái là một DAG (đồ thị có hướng không chu trình), ta tính trực tiếp bằng đệ quy có nhớ hoặc quy hoạch động theo thứ tự tô-pô.
- Nếu đồ thị trạng thái có chu trình (ví dụ: quay lại chính nó với xác suất $P$), ta thiết lập hệ phương trình tuyến tính và giải bằng **Khử Gauss (Gaussian Elimination)** trong $O(N^3)$.

---

## 2.5. Bit Manipulation & Linear Basis

### 1. Các thủ thuật Bitwise cơ bản và hàm nội tại (Built-in Intrinsics)
- `x & (x - 1)`: Tắt bit 1 thấp nhất (dùng để kiểm tra lũy thừa của 2: `(x & (x - 1)) == 0`).
- `x & (-x)`: Trích xuất bit 1 thấp nhất (Lowbit - hạt nhân của cây Fenwick).
- `__builtin_popcountll(x)`: Đếm số bit 1 trong $O(1)$ phần cứng.
- `__builtin_clzll(x)`: Đếm số bit 0 ở đầu (Count leading zeros $\implies$ tìm vị trí bit cao nhất $\approx \lfloor \log_2 x \rfloor$).
- `__builtin_ctzll(x)`: Đếm số bit 0 ở cuối (Count trailing zeros).

### 2. Duyệt mọi tập con của một Mask (Submask Enumeration)
Duyệt tất cả các mặt nạ con của mọi mặt nạ từ $0$ đến $2^N - 1$ trong tổng thời gian $O(3^N)$ thay vì $O(4^N)$:
```cpp
for (int mask = 0; mask < (1 << n); ++mask) {
    for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
        // sub là một tập con thực sự của mask
    }
}
```

### 3. Cơ sở tuyến tính (Linear Basis trên trường $\mathbb{F}_2$)
- **Bài toán:** Cho mảng $A$ gồm $N$ số ($A_i \le 2^{60}$). Tìm tập con có XOR lớn nhất, hoặc kiểm tra xem một số $X$ có thể tạo ra từ phép XOR của một tập con hay không.
- **Bản chất:** Mỗi số là một vector trong không gian vector 60 chiều trên trường modulo 2. Khử Gauss tìm tập hợp tối đa các vector độc lập tuyến tính (kích thước tối đa bằng số bit $B \le 60$).
```cpp
struct LinearBasis {
    long long basis[64];
    int sz = 0;
    LinearBasis() { memset(basis, 0, sizeof(basis)); }

    void insertVector(long long mask) {
        for (int i = 62; i >= 0; --i) {
            if ((mask >> i) & 1) {
                if (!basis[i]) {
                    basis[i] = mask;
                    sz++;
                    return;
                }
                mask ^= basis[i];
            }
        }
    }

    long long getMaxXor() {
        long long maxXor = 0;
        for (int i = 62; i >= 0; --i) {
            if ((maxXor ^ basis[i]) > maxXor) {
                maxXor ^= basis[i];
            }
        }
        return maxXor;
    }
};
```

---

## 2.6. Matrix Exponentiation (Lũy thừa ma trận)

### 1. Ứng dụng giải hệ thức truy hồi tuyến tính
Mọi hệ thức truy hồi dạng $F_n = c_1 F_{n-1} + c_2 F_{n-2} + \dots + c_k F_{n-k}$ đều có thể biểu diễn dưới dạng nhân vector trạng thái với ma trận chuyển tiếp bậc $K \times K$:
$$\begin{pmatrix} F_n \\ F_{n-1} \\ \vdots \\ F_{n-k+1} \end{pmatrix} = \begin{pmatrix} c_1 & c_2 & \dots & c_k \\ 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \end{pmatrix} \begin{pmatrix} F_{n-1} \\ F_{n-2} \\ \vdots \\ F_{n-k} \end{pmatrix}$$
Tính lũy thừa ma trận bằng Binary Exponentiation cho phép tìm $F_N$ với $N \le 10^{18}$ trong thời gian $O(K^3 \log N)$.

### 2. Đếm số đường đi độ dài $K$ trên đồ thị
Cho ma trận kề $A$ của đồ thị ($A_{ij} = 1$ nếu có cạnh nối $i \to j$). Khi đó, phần tử $(i, j)$ của ma trận $A^K$ chính là **số lượng đường đi có độ dài đúng bằng $K$ từ đỉnh $i$ đến đỉnh $j$**.

---

## 2.7. Invariant, Parity & Algebraic Transformations

### 1. Bất biến về Tính chẵn lẻ (Parity Invariant)
- **Tô màu bàn cờ (Chessboard Coloring):** Mỗi ô $(r, c)$ được gán màu $(r + c) \bmod 2$. Quân mã đi từ ô đen luôn sang ô trắng; lát gạch domino $1 \times 2$ luôn phủ đúng 1 ô đen và 1 ô trắng.
- **Số cặp nghịch thế (Inversion Parity):** Trò chơi 15-puzzle (xếp số trên bảng $4 \times 4$) có thể giải được khi và chỉ khi tính chẵn lẻ của số nghịch thế cộng với hàng của ô trống có cùng tính chẵn lẻ với cấu hình đích.

### 2. Kỹ thuật Biến đổi Đại số & Tách biến (Separation of Variables)
- **Biến đổi tổng đôi:** Khi gặp $\sum_{i=1}^N \sum_{j=1}^N |A_i - A_j|$, thay vì tính trực tiếp $O(N^2)$, ta sắp xếp mảng $A_1 \le A_2 \le \dots \le A_N$.
  Khoảng cách $|A_i - A_j| = A_i - A_j$ với mọi $i > j$.
  $$\sum_{i > j} (A_i - A_j) = \sum_{i=1}^N (2i - N - 1) A_i \implies \text{Tính trong } O(N \log N)!$$
- **Độc lập tọa độ:** Khi tính khoảng cách Manhattan $|x_1 - x_2| + |y_1 - y_2|$, hai chiều $X$ và $Y$ hoàn toàn độc lập $\implies$ Giải bài toán trên trục $X$ và trục $Y$ riêng biệt rồi cộng lại.

---

## 2.8. Nhận biết bài toán thuần Toán học (No-Algorithm Problem)

### Dấu hiệu nhận biết:
1. $N \le 10^{18}$, thời gian 1.0s, không cho mảng dữ liệu đầu vào cụ thể mà chỉ cho 2-3 số nguyên $N, M, K$.
2. Đề bài mô tả một trò chơi chia kẹo, di chuyển hạt sỏi, xóa số có quy luật rõ ràng.
3. Không thể thiết kế trạng thái DP vì không gian quá lớn ($10^{18}$), đồ thị không có đỉnh cụ thể.

### Giao thức xử lý bài toán thuần Toán học:
```
[Bước 1: Viết Brute Force] -> [Bước 2: Chạy với N = 1..20] -> [Bước 3: Lập bảng kết quả]
                                                                        |
[Bước 6: AC 100%] <- [Bước 5: Chứng minh quy nạp] <- [Bước 4: Nhận diện quy luật dãy số]
```

---
---

# CHƯƠNG 3: ALGORITHM PARADIGMS

> *"Thuật toán không phải là công thức nấu ăn. Thuật toán là tư duy tổ chức dữ liệu và định hướng luồng suy diễn."*

---

## 3.1. Brute Force, Recursion & Backtracking Pruning

### 1. Bản chất của Nhánh cận (Branch and Bound)
Khi không gian nghiệm dạng cây quá lớn (ví dụ $N!$ hoặc $2^N$), kỹ thuật nhánh cận cho phép "chặt tỉa" (prune) những cành cây đệ quy mà ta chứng minh được chắc chắn không chứa nghiệm tối ưu:
- **Tỉa khả thi (Feasibility Pruning):** Nếu tổng hiện tại đã vượt quá giới hạn cho phép, dừng đệ quy ngay lập tức (`if (current_sum > target) return;`).
- **Tỉa tối ưu (Optimality Pruning):** Nếu chi phí hiện tại cộng với chi phí ước lượng nhỏ nhất (Lower Bound) để đi tiếp vẫn lớn hơn chi phí tốt nhất đã tìm thấy ($best\_ans$), dừng đệ quy ngay (`if (cost + estimate_min >= best_ans) return;`).
- **Phá vỡ tính đối xứng (Symmetry Breaking):** Nếu các nghiệm chỉ khác nhau về thứ tự hoán vị của các tập con giống nhau, ép buộc thứ tự tăng dần để tránh duyệt trùng lặp $K!$ lần.

---

## 3.2. Divide and Conquer & Meet-in-the-Middle

### 1. Kỹ thuật Gặp nhau ở giữa (Meet in the Middle)
- **Khi nào sử dụng?** Khi $N \approx 36 - 44$. Duyệt toàn bộ $2^{40} \approx 10^{12}$ chắc chắn TLE.
- **Bản chất:**
  1. Chia tập $N$ phần tử thành 2 nửa: Nửa đầu kích thước $N/2$, nửa sau kích thước $N - N/2$.
  2. Sinh toàn bộ không gian nghiệm của nửa đầu vào mảng $Left$ ($2^{20} \approx 10^6$ trạng thái).
  3. Sinh toàn bộ không gian nghiệm của nửa sau vào mảng $Right$ ($2^{20} \approx 10^6$ trạng thái).
  4. Sắp xếp mảng $Right$. Với mỗi giá trị $x \in Left$, sử dụng Binary Search (`std::lower_bound`) trên $Right$ để tìm kiếm phần bù thích hợp.
  5. Độ phức tạp: $O(2^{N/2} \cdot \frac{N}{2})$, giảm thời gian từ hàng giờ xuống còn dưới $0.3$ giây!

---

## 3.3. Binary Search on Answer & Monotonicity

### 1. Bản chất của Tính đơn điệu (Monotonicity)
Một bài toán có thể áp dụng Chặt nhị phân trên kết quả khi và chỉ khi tồn tại một hàm kiểm tra vị từ (Predicate Function) $P(X) \in \{\text{True}, \text{False}\}$ thỏa mãn tính đơn điệu:
$$P(X) = \text{True} \implies P(X') = \text{True} \quad \forall X' \le X \quad (\text{hoặc ngược lại})$$

```
Không gian nghiệm: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Giá trị P(X):       T  T  T  T  T  F  F  F  F  F
                                ^
                            Đáp án cực đại thỏa mãn
```

### 2. Cài đặt chuẩn mực C++ chống lỗi lặp vô hạn (Infinite Loop) & Off-by-one
```cpp
// Tìm giá trị X LỚN NHẤT thỏa mãn check(X) == true
long long low = MIN_ANS, high = MAX_ANS;
long long ans = -1;

while (low <= high) {
    long long mid = low + (high - low) / 2;
    if (check(mid)) {
        ans = mid;         // Ghi nhận nghiệm hợp lệ khả dĩ
        low = mid + 1;     // Cố gắng tìm nghiệm lớn hơn ở nửa phải
    } else {
        high = mid - 1;    // Không thỏa mãn, thu hẹp về nửa trái
    }
}
```

---

## 3.4. Two Pointers & Sliding Window

### 1. Điều kiện áp dụng Hai con trỏ
Hai con trỏ $L$ và $R$ chỉ đạt độ phức tạp $O(N)$ khi:
- Cả con trỏ $L$ và con trỏ $R$ đều **chỉ dịch chuyển theo một chiều** (không bao giờ quay lùi).
- Khi mở rộng $R$, điều kiện bài toán biến thiên đơn điệu (ví dụ: tổng tăng lên, số lượng phần tử phân biệt tăng lên). Khi điều kiện bị vi phạm, ta tăng $L$ để tái lập lại điều kiện hợp lệ.

---

## 3.5. Sweep Line & Offline Queries

### 1. Bản chất của Kỹ thuật Đường quét (Sweep Line)
- Chuyển bài toán không gian 2D tĩnh thành một chuỗi sự kiện 1D theo thời gian.
- Tưởng tượng một đường thẳng quét từ trái sang phải dọc theo trục hoành $X$. Mỗi khi đường quét chạm vào một đối tượng, một **sự kiện (Event)** được kích hoạt:
  - Bắt đầu một đoạn thẳng/hình chữ nhật: Thêm vào cấu trúc dữ liệu lưu trạng thái hiện tại.
  - Kết thúc một đoạn thẳng/hình chữ nhật: Xóa khỏi cấu trúc dữ liệu.
  - Điểm truy vấn: Truy vấn trên cấu trúc dữ liệu hiện tại.

---

## 3.6. Dynamic Programming Deep Dive (Quy hoạch động chuyên sâu)

Quy hoạch động (DP) là chủ đề có tần suất xuất hiện cao nhất và phân loại thí sinh mạnh nhất.

### 1. Tư duy Tìm kiếm Trạng thái DP (State Discovery Protocol)
Để tìm trạng thái DP, hãy trả lời 3 câu hỏi theo thứ tự:
1. **Thông tin tối thiểu nào cần thiết để biết một bước chuyển là hợp lệ?**
   - Ví dụ: Trong bài toán chọn tập con không có 2 phần tử kề nhau, ta chỉ cần biết: "Phần tử liền trước có được chọn hay không?" $\implies$ Thêm chiều $0/1$.
2. **Hàm mục tiêu phụ thuộc vào những biến số nào?**
   - Vị trí hiện tại $i$, sức chứa còn lại $w$, số lượng phần tử đã chọn $k$.
3. **Có thể nén hoặc loại bỏ bớt chiều nào dựa trên toán học không?**
   - Nếu $i + j + k = \text{Const}$, ta chỉ cần lưu 2 biến $i$ và $j$, biến $k$ tự suy ra được $k = \text{Const} - i - j$.

### 2. Hai phong cách chuyển trạng thái: Pull vs Push DP
- **Pull DP (Kéo nghiệm về):**
  $$dp[i] = \min(dp[i-1], dp[i-2]) + cost[i]$$
  Trạng thái hiện tại tính từ các trạng thái đã biết trong quá khứ. Rất trực quan và dễ viết Base Case.
- **Push DP (Bắn nghiệm đi):**
  Từ trạng thái hiện tại $dp[i]$, cập nhật giá trị cho các trạng thái tương lai:
  $$dp[i+1] = \min(dp[i+1], dp[i] + cost), \quad dp[i+2] = \min(dp[i+2], dp[i] + cost)$$
  Cực kỳ hữu ích trong các bài toán xác suất hoặc khi việc xác định trạng thái cha khó hơn xác định trạng thái con.

### 3. Quy trình Tối ưu hóa từ Brute Force lên DP đỉnh cao:
```
[Bước 1: Hàm đệ quy ngây thơ] 
       ↓ (Thấy các bài toán con trùng lặp - Overlapping Subproblems)
[Bước 2: Memoization - Đệ quy có nhớ] 
       ↓ (Xóa bỏ chi phí gọi hàm Call-stack)
[Bước 3: Iterative DP - Bảng phương án lặp] 
       ↓ (Nhận thấy dp[i] chỉ phụ thuộc dp[i-1])
[Bước 4: Space Optimization - Giảm từ O(N^2) về O(N) bộ nhớ] 
       ↓ (Vòng lặp bên trong tìm Min/Max/Tổng)
[Bước 5: Data Structure Acceleration - Tăng tốc bằng SegTree, Monotonic Queue, CHT]
```

---

## 3.7. Specialized DP: Bitmask, Digit, Tree & Rerooting

### 1. Bitmask DP
- Biểu diễn tập hợp các phần tử đã chọn dưới dạng số nguyên nhị phân.
- Áp dụng khi $N \le 20$.
- Ví dụ kinh điển: Traveling Salesperson Problem (TSP) trong $O(N^2 \cdot 2^N)$:
  $dp(mask, u)$ là chi phí nhỏ nhất để thăm tập các đỉnh trong $mask$ và hiện đang đứng tại đỉnh $u$.

### 2. Digit DP (Quy hoạch động chữ số)
- **Vấn đề giải quyết:** Đếm số lượng các số trong đoạn $[A, B]$ ($A, B \le 10^{18}$) thỏa mãn một tính chất về chữ số.
- Chuyển bài toán thành $Solve(B) - Solve(A - 1)$.
- Bộ trạng thái chuẩn:
  `dp(idx, tight, leading_zero, sum_digits/mask)`
  - `idx`: Vị trí chữ số đang xét từ trái sang phải.
  - `tight`: Biến cờ boolean. Nếu `tight == true`, chữ số tiếp theo chỉ được chọn từ $0$ đến $Digit[idx]$. Nếu `tight == false`, chữ số tiếp theo được tự do chọn từ $0$ đến $9$.
  - `leading_zero`: Đang trong giai đoạn các số 0 vô nghĩa ở đầu (chưa hình thành số thực sự).

### 3. Tree DP (Quy hoạch động trên cây)
- Cây có cấu trúc đệ quy tự nhiên: Mỗi nút là gốc của một cây con.
- DFS tính toán giá trị của các nút lá trước, sau đó tổng hợp thông tin từ các nút con lên nút cha (Post-order Traversal).

### 4. Rerooting DP (Kỹ thuật Đổi gốc cây trong $O(N)$)
- **Vấn đề:** Cần tính kết quả của bài toán Tree DP với **mọi đỉnh $u \in [1, N]$ đều lần lượt được chọn làm gốc**.
- Nếu chạy Tree DP độc lập $N$ lần $\implies O(N^2)$ (TLE khi $N = 2 \cdot 10^5$).
- **Kỹ thuật Đổi gốc (2-pass DFS):**
  - **Pass 1 (Bottom-Up):** Chọn đỉnh 1 làm gốc tạm thời, tính mảng $dp[u]$ cho tất cả cây con hướng xuống dưới.
  - **Pass 2 (Top-Down):** Truyền kết quả từ nút cha xuống nút con. Khi chuyển gốc từ cha $u$ sang con $v$, ta chỉ cần "bóc tách" đóng góp của cây con $v$ ra khỏi $u$, rồi gộp phần còn lại của cây vào làm một nhánh con mới của $v$. Thời gian hoàn thành trong $O(N)$!

---

## 3.8. DP Optimization Techniques

1. **Prefix Sum Optimization:** Khi chuyển trạng thái có dạng $dp[i][j] = \sum_{k=L}^{R} dp[i-1][k]$, thay vì duyệt $k$ tốn $O(K)$, dùng mảng cộng dồn để truy vấn trong $O(1)$.
2. **Monotonic Queue Optimization:** Khi $dp[i] = \min_{i - K \le j < i} (dp[j] + cost(j))$, sử dụng `std::deque` duy trì các giá trị tăng dần để lấy cực trị trong $O(1)$ amortized.
3. **Convex Hull Trick (CHT):** Tối ưu hàm mục tiêu dạng $dp[i] = \min_{j < i} (dp[j] + M_j \cdot X_i + C_j)$ từ $O(N^2)$ xuống $O(N \log N)$ hoặc $O(N)$ bằng cách biểu diễn chuyển trạng thái như việc tìm bao lồi của tập các đường thẳng $y = M_j x + C_j$.

---
# CHƯƠNG 4: DATA STRUCTURES

> *"Cấu trúc dữ liệu là nghệ thuật tổ chức bộ nhớ sao cho thời gian truy vấn và cập nhật đạt đến giới hạn vật lý tối thiểu."*

Mỗi cấu trúc dữ liệu sinh ra để giải quyết một sự đánh đổi (Trade-off) cụ thể giữa **chi phí cập nhật** (Update Cost) và **chi phí truy vấn** (Query Cost).

---

## 4.1. Modern C++ STL & Custom Allocators / Hash

### 1. `std::vector`, `std::deque`, `std::list`
- **`std::vector`:** Luôn là lựa chọn số 1 nhờ tính liên tục của bộ nhớ (Cache-friendly). Sử dụng `reserve(N)` để tránh tái cấp phát bộ nhớ $O(N)$ ngầm định.
- **`std::deque`:** Thích hợp cho 0-1 BFS và Monotonic Queue, cho phép `push_front`/`pop_front` trong $O(1)$.
- **`std::list`:** Rất ít dùng trong CP do con trỏ rời rạc gây Cache Miss trầm trọng.

### 2. Nguy cơ bị Hack của `std::unordered_map` và Giải pháp Custom Hash
- `std::unordered_map` có độ phức tạp trung bình $O(1)$, nhưng hàm băm mặc định của GCC rất dễ bị khai thác bởi các Anti-Hash Test trên Codeforces, khiến số vụ xung đột (Hash Collisions) tăng vọt, đẩy thời gian chạy lên $O(N^2)$ (TLE).
- **Bộ băm an toàn chống Hack (Custom Safe Hash):**
```cpp
#include <chrono>

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = 
            std::chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

// Khai báo an toàn tuyệt đối trên Codeforces:
// std::unordered_map<long long, int, custom_hash> safe_map;
```

### 3. Cạm bẫy chết người khi xóa phần tử trong `std::multiset`
```cpp
std::multiset<int> ms = {5, 5, 5, 7};
// CÁCH SAI: Xóa TẤT CẢ các số 5 có trong multiset
ms.erase(5); // multiset chỉ còn {7} !

// CÁCH ĐÚNG: Chỉ xóa ĐÚNG MỘT phần tử số 5
auto it = ms.find(5);
if (it != ms.end()) {
    ms.erase(it); // multiset còn lại {5, 5, 7}
}
```

---

## 4.2. Monotonic Stack & Monotonic Queue

### 1. Monotonic Stack (Ngăn xếp đơn điệu)
- **Vấn đề giải quyết:** Tìm phần tử đầu tiên lớn hơn/nhỏ hơn về bên trái/bên phải của mọi vị trí trong mảng $O(N)$.
- **Cài đặt chuẩn C++:**
```cpp
// Tìm chỉ số phần tử nhỏ hơn gần nhất về bên trái (Nearest Smaller to Left)
std::vector<int> nearestSmallerLeft(const std::vector<int>& a) {
    int n = a.size();
    std::vector<int> res(n, -1);
    std::vector<int> st; // Lưu index, giá trị tăng dần
    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.back()] >= a[i]) {
            st.pop_back();
        }
        res[i] = st.empty() ? -1 : st.back();
        st.push_back(i);
    }
    return res;
}
```

### 2. Monotonic Queue (Hàng đợi đơn điệu)
- **Vấn đề giải quyết:** Tìm giá trị lớn nhất/nhỏ nhất trong cửa sổ trượt (Sliding Window) độ dài $K$ khi cửa sổ di chuyển từ trái sang phải trong $O(N)$ tổng thời gian ($O(1)$ amortized mỗi bước).
- **Cài đặt chuẩn C++:**
```cpp
std::vector<int> slidingWindowMin(const std::vector<int>& a, int k) {
    int n = a.size();
    std::vector<int> res;
    std::deque<int> dq; // Lưu index, giá trị a[index] tăng dần

    for (int i = 0; i < n; ++i) {
        // 1. Loại bỏ các phần tử nằm ngoài cửa sổ [i - k + 1, i]
        if (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        
        // 2. Duy trì tính đơn điệu: Loại bỏ các phần tử lớn hơn a[i]
        while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();

        dq.push_back(i);

        // 3. Ghi nhận kết quả khi cửa sổ đã đủ kích thước k
        if (i >= k - 1) res.push_back(a[dq.front()]);
    }
    return res;
}
```

---

## 4.3. Disjoint Set Union (DSU) & Rollback DSU

### 1. Vấn đề giải quyết
Quản lý các tập hợp không giao nhau, thực hiện thao tác hợp nhất 2 tập hợp (`unite`) và kiểm tra 2 phần tử có cùng tập hợp hay không (`find`) trong thời gian gần như hằng số $O(\alpha(N))$.

### 2. Cài đặt C++ hiện đại với Union by Size và Path Compression
```cpp
struct DSU {
    std::vector<int> parent, sz;
    int num_components;

    DSU(int n) : parent(n + 1), sz(n + 1, 1), num_components(n) {
        std::iota(parent.begin(), parent.end(), 0);
    }

    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]); // Path compression
    }

    bool unite(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u == root_v) return false;

        // Union by size
        if (sz[root_u] < sz[root_v]) std::swap(root_u, root_v);
        parent[root_v] = root_u;
        sz[root_u] += sz[root_v];
        num_components--;
        return true;
    }

    bool same(int u, int v) { return find(u) == find(v); }
};
```

### 3. DSU with Rollbacks (Dùng cho Offline Dynamic Connectivity)
- **Khi nào sử dụng?** Khi cần hoàn tác lại các thao tác `unite` trước đó (dùng trong chia để trị trên cây truy vấn thời gian).
- **Lưu ý sống còn:** KHÔNG ĐƯỢC dùng Path Compression khi cần Rollback, chỉ dùng **Union by Rank/Size** để giữ độ sâu cây ở mức $O(\log N)$, từ đó có thể rollback trạng thái trong $O(1)$.

---

## 4.4. Fenwick Tree (Binary Indexed Tree - BIT)

### 1. Vấn đề giải quyết
Cập nhật một phần tử tại vị trí $p$ và tính tổng tiền tố từ $1$ đến $p$ trên mảng động trong $O(\log N)$. Tiết kiệm bộ nhớ gấp 4 lần và chạy nhanh hơn Segment Tree từ 2 đến 3 lần.

### 2. Cài đặt chuẩn C++ (1-based Indexing)
```cpp
template <typename T>
struct FenwickTree {
    int n;
    std::vector<T> tree;

    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, T delta) {
        for (; i <= n; i += i & (-i)) tree[i] += delta;
    }

    T query(int i) const {
        T sum = 0;
        for (; i > 0; i -= i & (-i)) sum += tree[i];
        return sum;
    }

    T queryRange(int l, int r) const {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};
```

---

## 4.5. Segment Tree & Lazy Propagation

### 1. Vấn đề giải quyết
Thực hiện các truy vấn trên đoạn (Range Sum, Range Min/Max, Range GCD) và cập nhật một điểm (Point Update) hoặc một đoạn (Range Update) trong thời gian $O(\log N)$.

### 2. Cài đặt C++ Segment Tree với Lazy Propagation (Range Add, Range Sum)
```cpp
struct LazySegmentTree {
    int n;
    std::vector<long long> tree, lazy;

    LazySegmentTree(int n) : n(n), tree(4 * n, 0), lazy(4 * n, 0) {}

    void push(int node, int start, int end) {
        if (lazy[node] != 0) {
            int mid = (start + end) / 2;
            // Áp dụng giá trị lazy cho hai nút con
            tree[2 * node] += lazy[node] * (mid - start + 1);
            lazy[2 * node] += lazy[node];
            tree[2 * node + 1] += lazy[node] * (end - mid);
            lazy[2 * node + 1] += lazy[node];
            lazy[node] = 0; // Xóa lazy tại nút hiện tại
        }
    }

    void updateRange(int node, int start, int end, int l, int r, long long val) {
        if (r < start || end < l) return;
        if (l <= start && end <= r) {
            tree[node] += val * (end - start + 1);
            lazy[node] += val;
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateRange(2 * node, start, mid, l, r, val);
        updateRange(2 * node + 1, mid + 1, end, l, r, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    long long queryRange(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        push(node, start, end);
        int mid = (start + end) / 2;
        return queryRange(2 * node, start, mid, l, r) +
               queryRange(2 * node + 1, mid + 1, end, l, r);
    }
};
```

---

## 4.6. Sparse Table & Binary Lifting

### 1. Sparse Table (Bảng thưa)
- **Vấn đề giải quyết:** Static Range Minimum Query (RMQ) trên mảng tĩnh trong thời gian $O(1)$ sau khi tiền xử lý $O(N \log N)$.
- **Bản chất Idempotent:** Phép toán $\min(x, x) = x$ và $\gcd(x, x) = x$ cho phép hai đoạn phủ chồng lên nhau mà không làm sai lệch kết quả.
```cpp
struct SparseTable {
    int n, K;
    std::vector<std::vector<int>> st;
    std::vector<int> lg;

    SparseTable(const std::vector<int>& a) {
        n = a.size();
        K = 32 - __builtin_clz(n);
        st.assign(K, std::vector<int>(n));
        lg.assign(n + 1, 0);
        for (int i = 2; i <= n; ++i) lg[i] = lg[i / 2] + 1;

        st[0] = a;
        for (int j = 1; j < K; ++j) {
            for (int i = 0; i + (1 << j) <= n; ++i) {
                st[j][i] = std::min(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
            }
        }
    }

    int queryMin(int l, int r) {
        int j = lg[r - l + 1];
        return std::min(st[j][l], st[j][r - (1 << j) + 1]);
    }
};
```

---

## 4.7. Trie & Binary Trie

### 1. Trie Tiền tố xâu
- Quản lý từ điển, tìm kiếm tiền tố xâu ký tự trong $O(|S|)$.

### 2. Binary Trie (Trie nhị phân giải bài toán Max XOR)
- Biểu diễn các số nguyên dưới dạng chuỗi nhị phân cố định 30 hoặc 60 bit từ bit cao nhất (MSB) đến bit thấp nhất (LSB).
- **Tìm $\max(X \oplus A_i)$:** Tại mỗi bước xét bit thứ $k$ của $X$, nếu bit đó là $b$, ta ưu tiên rẽ sang nhánh có bit đối lập $1 - b$ để phép XOR tạo ra bit 1 tại vị trí đó!
- Thời gian truy vấn $O(B)$ với $B \le 30$ hoặc $60$.

---

## 4.8. Ordered Set (`__gnu_pbds`)

### 1. Vấn đề giải quyết
`std::set` chuẩn không hỗ trợ tìm phần tử lớn thứ $K$ hoặc tìm vị trí/thứ hạng của một giá trị. `pb_ds` (Policy Based Data Structures) tích hợp sẵn trong thư viện GCC cung cấp Red-Black Tree với 2 phương thức cực mạnh chạy trong $O(\log N)$:
1. `find_by_order(k)`: Trả về con trỏ tới phần tử có thứ tự thứ $k$ (0-indexed).
2. `order_of_key(x)`: Đếm số lượng phần tử strictly nhỏ hơn $x$.

```cpp
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;

template <typename T>
using ordered_set = tree<T, null_type, std::less<T>, rb_tree_tag, tree_order_statistics_node_update>;

// Cách dùng:
// ordered_set<int> os;
// os.insert(5); os.insert(10); os.insert(2);
// *os.find_by_order(0) -> 2 (nhỏ nhất)
// os.order_of_key(6)   -> 2 (có hai số 2 và 5 nhỏ hơn 6)
```

---

## 4.9. Persistent Segment Tree (Cây phân đoạn bền vững)

### 1. Vấn đề giải quyết
Lưu lại lịch sử của cây Segment Tree sau mỗi lần cập nhật mà không tốn $O(N)$ bộ nhớ. Cho phép truy vấn trên bất kỳ phiên bản nào trong quá khứ $O(\log N)$.
- **Ứng dụng kinh điển:** Range K-th Smallest Query (Tìm số nhỏ thứ $K$ trên đoạn $[L, R]$ bất kỳ mà không cần xử lý offline).

### 2. Bản chất cấu trúc
Mỗi lần cập nhật một điểm, thay vì sửa trực tiếp trên nút cũ, ta **tạo ra một nút mới** cho nút bị thay đổi và sao chép con trỏ tới các nút con không bị ảnh hưởng. Vì cây Segment Tree có độ sâu $\log N$, mỗi lần cập nhật chỉ tạo thêm tối đa $\log N$ nút mới!

---
---

# CHƯƠNG 5: GRAPH ALGORITHMS

> *"Đồ thị là ngôn ngữ vạn năng của khoa học máy tính: Mọi bài toán tối ưu hóa quan hệ đều quy về đồ thị."*

---

## 5.1. Graph Traversals & Topological Ordering

### 1. BFS vs DFS
- **BFS (Breadth-First Search):** Sử dụng hàng đợi (`std::queue`). Khám phá theo từng lớp độ sâu. Tìm đường đi ngắn nhất trên đồ thị không trọng số trong $O(V + E)$.
- **DFS (Depth-First Search):** Sử dụng ngăn xếp hoặc đệ quy. Khám phá sâu nhất có thể trước khi quay lui. Dùng để tìm thành phần liên thông, chu trình, thành phần song liên thông, khớp, cầu.

### 2. Sắp xếp tô-pô (Topological Sort)
- **Điều kiện tồn tại:** Chỉ tồn tại trên **DAG (Directed Acyclic Graph - Đồ thị có hướng không chu trình)**.
- **Thuật toán Kahn (In-degree Queue):**
  1. Tính bán bậc vào (In-degree) của mọi đỉnh.
  2. Đẩy tất cả đỉnh có In-degree bằng 0 vào hàng đợi.
  3. Lấy đỉnh $u$ ra, thêm vào thứ tự tô-pô, giảm In-degree của các đỉnh kề $v$. Nếu In-degree của $v$ về 0, đẩy $v$ vào hàng đợi.
  4. Nếu số đỉnh lấy ra $< V$, đồ thị có chu trình!

---

## 5.2. Shortest Paths

### 1. Thuật toán Dijkstra
- **Điều kiện:** Trọng số cạnh **không âm** ($w \ge 0$).
- **Độ phức tạp:** $O((V + E) \log V)$ sử dụng `std::priority_queue`.
```cpp
std::vector<long long> dijkstra(int start, int n, const std::vector<std::vector<std::pair<int, int>>>& adj) {
    const long long INF = 1e18;
    std::vector<long long> dist(n + 1, INF);
    std::priority_queue<std::pair<long long, int>, 
                        std::vector<std::pair<long long, int>>, 
                        std::greater<std::pair<long long, int>>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue; // Nút đã được cập nhật đường đi ngắn hơn

        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```

### 2. 0-1 BFS
- Khi trọng số cạnh chỉ gồm 2 loại $\{0, 1\}$.
- Dùng `std::deque`: Cạnh trọng số 0 đẩy vào **đầu** hàng đợi (`push_front`), cạnh trọng số 1 đẩy vào **cuối** hàng đợi (`push_back`). Thời gian $O(V + E)$ - nhanh hơn Dijkstra $\log V$ lần.

### 3. Bellman-Ford & Phát hiện Chu trình âm
- Cho phép trọng số cạnh âm. Chạy $V - 1$ vòng lặp nới lỏng cạnh.
- Nếu ở vòng lặp thứ $V$ vẫn có cạnh tiếp tục nới lỏng được $\implies$ Đồ thị tồn tại chu trình âm. Độ phức tạp $O(V \cdot E)$.

### 4. Floyd-Warshall
- Tìm đường đi ngắn nhất giữa mọi cặp đỉnh trong $O(V^3)$.
```cpp
for (int k = 1; k <= n; ++k)
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
```

---

## 5.3. Minimum Spanning Tree: Kruskal & Prim

### 1. Thuật toán Kruskal
- Sắp xếp tất cả các cạnh theo trọng số tăng dần $O(E \log E)$.
- Lần lượt xét từng cạnh: Nếu 2 đỉnh chưa thuộc cùng thành phần liên thông (kiểm tra bằng DSU), thêm cạnh đó vào cây khung và hợp nhất 2 đỉnh trong $O(\alpha(V))$.
- Tối ưu khi đồ thị thưa ($E \approx V$).

---

## 5.4. Connectivity: Tarjan SCC, Bridges, Articulation Points

### 1. Thành phần liên thông mạnh (SCC) - Thuật toán Tarjan
- Sử dụng hai mảng `tin[u]` (thời điểm vào) và `low[u]` (thời điểm vào nhỏ nhất vươn tới được qua các cạnh ngược).
- Khi kết thúc duyệt đỉnh $u$, nếu `low[u] == tin[u]`, toàn bộ các đỉnh trong ngăn xếp từ $u$ trở lên tạo thành một thành phần liên thông mạnh (SCC).
- Đồ thị ngưng kết (Condensation Graph) của các SCC luôn là một **DAG**.

### 2. Khớp và Cầu (Bridges & Articulation Points)
- Cạnh $(u, v)$ là Cầu khi và chỉ khi: `low[v] > tin[u]`.
- Đỉnh $u$ là Khớp khi:
  - $u$ là gốc cây DFS và có từ 2 con độc lập trở lên.
  - $u$ không phải là gốc cây DFS và tồn tại con $v$ thỏa mãn: `low[v] >= tin[u]`.

---

## 5.5. Tree Algorithms

### 1. Đường kính của Cây (Tree Diameter)
- **Thuật toán 2 lần BFS/DFS:**
  1. BFS từ một đỉnh bất kỳ $A$ để tìm đỉnh $U$ xa nhất.
  2. BFS từ đỉnh $U$ để tìm đỉnh $V$ xa nhất. Khoảng cách giữa $U$ và $V$ chính là đường kính của cây!
  - Luôn đúng trên đồ thị cây có trọng số không âm.

### 2. Tổ tiên chung gần nhất (LCA) bằng Binary Lifting
- Tiền xử lý bảng `up[node][k]` là tổ tiên thứ $2^k$ của `node` trong $O(N \log N)$.
- Nâng hai đỉnh về cùng độ sâu, sau đó đồng thời nhảy các bước nhảy nhị phân lớn nhất để tìm LCA trong $O(\log N)$.

### 3. Kỹ thuật Trải phẳng Cây (Euler Tour Technique)
- Đi vào đỉnh $u$: Ghi nhận thời điểm `tin[u]`. Đi ra khỏi $u$: Ghi nhận `tout[u]`.
- Cây con gốc $u$ trở thành một đoạn con liên tiếp trên mảng 1D: $[tin[u], tout[u]]$. Mọi thao tác cập nhật/truy vấn trên cây con được quy về bài toán trên đoạn với Segment Tree hoặc Fenwick Tree!

---

## 5.6. Network Flow & Bipartite Matching

### 1. Định lý Luồng cực đại - Lát cắt cực tiểu (Max-Flow Min-Cut Theorem)
Giá trị của luồng cực đại từ nguồn $S$ đến đích $T$ bằng dung lượng nhỏ nhất của một lát cắt ngăn cách $S$ và $T$.

### 2. Thuật toán Dinic
- Sử dụng đồ thị phân tầng (Level Graph) bằng BFS và tìm đường tăng luồng chặn (Blocking Flow) bằng DFS.
- Độ phức tạp: $O(V^2 E)$ trên mạng tổng quát, và $O(E \sqrt{V})$ trên mạng đơn vị (Unit Networks) - giải bài toán Cặp ghép cực đại đồ thị hai phía cực nhanh trong thời gian thực.

---

## 5.7. 2-Satisfiability (2-SAT)

### 1. Bản chất
Tìm phép gán chân trị cho các biến Boolean thỏa mãn biểu thức dạng hội của các mệnh đề tuyển:
$$(x_1 \lor x_2) \land (\neg x_1 \lor x_3) \land \dots$$
- Mệnh đề $(a \lor b)$ tương đương với hai cạnh suy diễn: $(\neg a \implies b)$ và $(\neg b \implies a)$.
- Xây dựng đồ thị có hướng: Biến $x$ và phủ định $\neg x$ là các đỉnh.
- Biểu thức thỏa mãn khi và chỉ khi: **Không có biến $x$ nào mà $x$ và $\neg x$ cùng thuộc một thành phần liên thông mạnh (SCC)**!

---
---

# CHƯƠNG 6: STRING ALGORITHMS

> *"Xử lý chuỗi là cuộc chiến giữa tính tuần hoàn của ký tự và sự bùng nổ tổ hợp của tiền tố/hậu tố."*

---

## 6.1. String Hashing (Băm chuỗi an toàn)

### 1. Polynomial Rolling Hash
Gán mỗi chuỗi $S = s_0 s_1 \dots s_{n-1}$ một giá trị băm:
$$\text{Hash}(S) = \left( \sum_{i=0}^{n-1} s_i \cdot B^{n-1-i} \right) \bmod M$$
Truy vấn mã băm của xâu con $S[L..R]$ trong $O(1)$:
$$\text{Hash}(S[L..R]) = (\text{PrefixHash}[R+1] - \text{PrefixHash}[L] \cdot B^{R - L + 1}) \bmod M$$

### 2. Chiến lược chống Hash Collision trong Contest
- **Không bao giờ dùng Modulo $2^{64}$ (tràn số `unsigned long long` tự nhiên):** Đã có các bộ test sinh sẵn đánh gãy modulo $2^{64}$ bằng nghịch lý Thue-Morse!
- **Sử dụng Double Hash:** Băm đồng thời với 2 modulo lớn độc lập (ví dụ $M_1 = 10^9 + 7, M_2 = 10^9 + 9$) hoặc modulo an toàn $M = 2^{61} - 1$ (số nguyên tố Mersenne).

---

## 6.2. KMP (Knuth-Morris-Pratt) & Prefix Function

### 1. Hàm tiền tố $\pi[i]$ (Pi Table)
$\pi[i]$ là độ dài của tiền tố thực sự dài nhất của $S[0..i]$ đồng thời là hậu tố của $S[0..i]$.
Tính toàn bộ mảng $\pi$ trong $O(N)$.
```cpp
std::vector<int> computePi(const std::string& s) {
    int n = s.length();
    std::vector<int> pi(n, 0);
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    return pi;
}
```

---

## 6.3. Z-Algorithm

### 1. Mảng $Z[i]$
$Z[i]$ là độ dài tiền tố chung dài nhất (Longest Common Prefix - LCP) giữa chuỗi $S$ và chuỗi con bắt đầu từ vị trí $i$ của $S$.
Tính mảng $Z$ trong $O(N)$ bằng kỹ thuật duy trì đoạn $[L, R]$ xa nhất về bên phải (Z-box).

---

## 6.4. Aho-Corasick Automaton

### 1. Vấn đề giải quyết
Tìm kiếm đồng thời nhiều chuỗi mẫu (Multi-pattern Matching) trong một văn bản lớn trong thời gian $O(|Text| + \sum |Pattern|)$.
- Dựng cây Trie chứa tất cả các chuỗi mẫu.
- Xây dựng các liên kết thất bại (Failure Links) tương tự hàm $\pi$ của KMP bằng BFS.

---

## 6.5. Suffix Array & LCP Array

### 1. Suffix Array (Mảng hậu tố)
Một mảng chứa các chỉ số bắt đầu của tất cả các hậu tố của chuỗi $S$, được sắp xếp theo thứ tự từ điển.
- Thuật toán nhân đôi (Doubling Algorithm): $O(N \log N)$ hoặc $O(N \log^2 N)$.
- Kết hợp với **Thuật toán Kasai** tính mảng LCP (Longest Common Prefix giữa các hậu tố kề nhau trong Suffix Array) trong $O(N)$.
- Cho phép giải quyết hầu hết mọi bài toán xử lý xâu nâng cao (đếm số xâu con phân biệt, tìm xâu con lặp lại nhiều lần nhất).

---

## 6.6. Manacher's Algorithm for Palindromes

Tìm tất cả các xâu con đối xứng (Palindromes) trong một xâu ký tự trong thời gian tuyến tính đúng $O(N)$ bằng cách tận dụng tính chất đối xứng qua tâm của các xâu đối xứng đã tìm thấy trước đó.

---
# CHƯƠNG 7: ADVANCED TOPICS

> *"Kỹ thuật nâng cao không phải là thứ để phô trương; chúng là chiếc chìa khóa duy nhất để mở những cánh cửa mang tên ICPC World Finals."*

---

## 7.1. Phân tầng kiến thức thi đấu

Để việc ôn luyện đạt hiệu suất cao nhất và không bị quá tải, toàn bộ khối lượng kiến thức được phân định rõ ràng thành 3 cấp độ:

```
+-------------------------------------------------------------------------+
| CẤP ĐỘ 3: CHUYÊN SÂU (ICPC World Finals / Grandmaster)                 |
| - FFT / NTT / Polynomial Ops                                            |
| - Link-Cut Tree, Treap, Persistent Data Structures                      |
| - Suffix Automaton, Palindromic Tree (Eertree)                         |
| - Min-Cost Max-Flow, Simplex Algorithm                                  |
+-------------------------------------------------------------------------+
                                    ↑
+-------------------------------------------------------------------------+
| CẤP ĐỘ 2: MỤC TIÊU ICPC 2027 (Regional & National)                      |
| - Heavy-Light Decomposition (HLD) & Centroid Decomposition              |
| - Convex Hull Trick (CHT) & Li Chao Tree                                |
| - Divide and Conquer DP Optimization                                    |
| - Mo's Algorithm & Mo on Trees                                          |
| - Computational Geometry: Convex Hull, Point in Polygon                 |
| - 2-SAT, Dinic's Algorithm, Hopcroft-Karp                               |
| - Suffix Array + LCP                                                    |
+-------------------------------------------------------------------------+
                                    ↑
+-------------------------------------------------------------------------+
| CẤP ĐỘ 1: THIẾT YẾU CHO KỲ THI THÁNG 12/2026 (Nền tảng sống còn)       |
| - STL thuần thục, Two Pointers, Sliding Window, Binary Search Answer    |
| - Prefix Sums, Difference Array, Fenwick Tree, Segment Tree + Lazy      |
| - DP cơ bản, 2D DP, DP Knapsack, Bitmask DP, Tree DP                    |
| - Graph: BFS, DFS, Dijkstra, Kruskal, DSU, LCA Binary Lifting           |
| - Number Theory: Sàng Eratosthenes, Modulo Inverse, Tổ hợp nCr         |
| - String Hashing, KMP                                                   |
+-------------------------------------------------------------------------+
```

---

## 7.2. Computational Geometry (Hình học tính toán)

### 1. Cấu trúc Điểm và Vector 2D chuẩn C++
```cpp
struct Point {
    long long x, y;
    Point operator-(const Point& other) const { return {x - other.x, y - other.y}; }
    long long cross(const Point& other) const { return x * other.y - y * other.x; }
    long long dot(const Point& other) const { return x * other.x + y * other.y; }
};

// Kiểm tra hướng rẽ: > 0 là rẽ trái (CCW), < 0 là rẽ phải (CW), = 0 là thẳng hàng
long long crossProduct(Point a, Point b, Point c) {
    return (b - a).cross(c - a);
}
```

### 2. Bao lồi (Convex Hull) - Thuật toán Monotone Chain ($O(N \log N)$)
Thuật toán của Andrew sắp xếp các điểm theo tọa độ $x$, sau đó dựng riêng biệt Bao lồi dưới (Lower Hull) và Bao lồi trên (Upper Hull):
```cpp
std::vector<Point> convexHull(std::vector<Point>& pts) {
    int n = pts.size(), k = 0;
    if (n <= 2) return pts;
    std::vector<Point> h(2 * n);

    std::sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        return a.x < b.x || (a.x == b.x && a.y < b.y);
    });

    // Dựng Lower Hull
    for (int i = 0; i < n; ++i) {
        while (k >= 2 && crossProduct(h[k - 2], h[k - 1], pts[i]) <= 0) k--;
        h[k++] = pts[i];
    }
    // Dựng Upper Hull
    for (int i = n - 2, t = k + 1; i >= 0; --i) {
        while (k >= t && crossProduct(h[k - 2], h[k - 1], pts[i]) <= 0) k--;
        h[k++] = pts[i];
    }
    h.resize(k - 1);
    return h;
}
```

---

## 7.3. Advanced DP Optimizations

### 1. Convex Hull Trick (CHT)
- Dạng hàm mục tiêu: $dp[i] = \min_{j < i} (dp[j] + M_j \cdot X_i + C_j)$.
- Khi các hệ số góc $M_j$ và điểm truy vấn $X_i$ đều tăng đơn điệu: Dùng `std::deque` duy trì các đường thẳng trên bao lồi trong $O(N)$ tổng thời gian.
- Khi không có tính đơn điệu: Dùng **Cây Li Chao (Li Chao Tree)** hoặc `std::set` động (Dynamic CHT) để thêm đường thẳng và truy vấn trong $O(N \log N)$.

### 2. Divide and Conquer DP Optimization
- Áp dụng khi hàm chi phí thỏa mãn **Bất đẳng thức Tứ giác (Quadrangle Inequality)**:
  $$C(a, c) + C(b, d) \le C(a, d) + C(b, c) \quad \text{với mọi } a \le b \le c \le d$$
  Kéo theo tính chất đơn điệu của điểm chia tối ưu: $opt[i][j-1] \le opt[i][j] \le opt[i+1][j]$.
- Thuật toán chia để trị giảm độ phức tạp từ $O(K \cdot N^2)$ xuống $O(K \cdot N \log N)$.

---

## 7.4. Heavy-Light Decomposition (HLD) & Centroid Decomposition

### 1. Phân rã Nhẹ - Nặng (HLD)
- **Vấn đề giải quyết:** Cập nhật trọng số trên đường đi giữa 2 đỉnh $(u, v)$ bất kỳ trên cây và truy vấn trong $O(\log^2 N)$.
- **Bản chất:**
  - Cạnh từ cha xuống con có cây con lớn nhất gọi là **Heavy Edge**, các cạnh còn lại là **Light Edge**.
  - Các cạnh nặng nối tiếp nhau tạo thành các chuỗi nặng (**Heavy Chains**).
  - Khi đi từ nút bất kỳ lên gốc, ta chỉ đi qua tối đa $O(\log N)$ chuỗi nhẹ.
  - Toàn bộ cây được ánh xạ vào một mảng 1D sao cho mỗi Heavy Chain là một đoạn liên tiếp $\implies$ Dùng Segment Tree quản lý trực tiếp!

### 2. Phân rã Trọng tâm Cây (Centroid Decomposition)
- **Trọng tâm của cây (Centroid):** Là đỉnh mà khi loại bỏ nó, mỗi thành phần liên thông còn lại có kích thước không quá $\lfloor N/2 \rfloor$.
- **Bản chất:** Đệ quy tìm trọng tâm, giải quyết mọi đường đi đi qua trọng tâm trong $O(\text{Size})$, sau đó xóa trọng tâm và đệ quy xuống các cây con.
- Cây trọng tâm có độ sâu tối đa $O(\log N)$, đưa mọi bài toán đếm đường đi trên cây về độ phức tạp $O(N \log N)$.

---

## 7.5. Mo's Algorithm & Square Root Decomposition

### 1. Thuật toán Mo (Offline Range Queries)
- **Điều kiện:** Đọc toàn bộ các truy vấn trước (Offline), và từ kết quả của đoạn $[L, R]$ có thể mở rộng hoặc thu hẹp sang $[L \pm 1, R \pm 1]$ trong $O(1)$ hoặc $O(\log N)$.
- **Thuật toán:**
  - Chia mảng thành các khối kích thước $B = \lceil \frac{N}{\sqrt{Q}} \rceil$.
  - Sắp xếp các truy vấn $(L_i, R_i)$ theo khóa:
    $$\text{Khối } \lfloor L_i / B \rfloor \text{ tăng dần, nếu trùng khối thì sắp xếp } R_i \text{ xen kẽ tăng/giảm (Zig-zag / Hilbert Curve)}.$$
  - Di chuyển hai con trỏ $curL$ và $curR$ để trả lời mọi truy vấn trong tổng thời gian $O((N + Q) \sqrt{N})$.

---

## 7.6. FFT / NTT (Biến đổi Fourier nhanh)

- **Vấn đề giải quyết:** Nhân hai đa thức bậc $N$ trong thời gian $O(N \log N)$ thay vì $O(N^2)$.
- **Ứng dụng trong CP:**
  - Mọi bài toán đếm số cách chọn cặp có tổng $A_i + A_j = S$ đều quy về tích chập (Convolution) của hai đa thức:
    $$P(x) = \sum x^{A_i} \implies P(x)^2 = \sum c_S x^S \implies c_S \text{ là số cách tạo ra tổng } S.$$
  - NTT (Number Theoretic Transform) thay thế số phức bằng căn nguyên thủy theo modulo nguyên tố NTT-friendly ($998244353 = 119 \cdot 2^{23} + 1$).

---
---

# CHƯƠNG 8: CONTEST STRATEGY

> *"Trong thi đấu đỉnh cao, chiến thuật quản lý thời gian và tâm lý vững vàng quyết định 50% số điểm của bạn."*

---

## 8.1. Đọc đề và Phân tích Constraints

### Quy trình 3 bước khi tiếp cận bài toán:
1. **Đọc Statement không dùng chuột:** Đọc lướt để hiểu câu chuyện, sau đó gạch chân các dữ kiện số học: Giới hạn mảng, khoảng giá trị của phần tử, đồ thị có cho phép đa cạnh/khuyên hay không.
2. **Kiểm tra Constraints để khóa vùng thuật toán:**
   - $N \le 2000 \implies$ Thuật toán $O(N^2)$ được chấp nhận. Đừng cố gắng nghĩ $O(N \log N)$ cho mất thời gian!
   - $N \le 2 \cdot 10^5 \implies$ Bắt buộc phải là $O(N)$ hoặc $O(N \log N)$.
   - $N \le 10^{18} \implies O(\log N)$ (Matrix Exp, Binary Search) hoặc công thức Toán $O(1)$.
3. **Phân tích bộ nhớ (Memory Limit):**
   - 256 MB $\approx 6 \cdot 10^7$ phần tử `int`.
   - Một mảng hai chiều `dp[5000][5000]` kiểu `int` chiếm $5000 \times 5000 \times 4 \text{ bytes} \approx 100 \text{ MB}$ (an toàn).
   - Nhưng `dp[10000][10000]` sẽ tốn $400 \text{ MB} \implies$ **Memory Limit Exceeded (MLE)** ngay lập tức!

---

## 8.2. Debugging & Kỹ thuật đỉnh cao

### 1. Tận dụng AddressSanitizer khi chạy trên máy cá nhân
Thêm cờ biên dịch để phát hiện ngay lập tức lỗi tràn mảng (Out of Bounds), truy cập con trỏ rác hoặc tràn ngăn xếp đệ quy:
```bash
g++ -O2 -std=c++20 -fsanitize=address,undefined -Wall -Wextra sol.cpp -o sol
```

### 2. Sử dụng `assert()` để bảo vệ giả thiết
Nếu bạn có một giả thiết quan trọng (ví dụ: $K \le N$, hoặc đồ thị không chu trình), hãy đặt `assert(K <= N)` trong code. Nếu giả thiết sai, chương trình sẽ báo RE (Runtime Error) ngay thay vì âm thầm trả về kết quả sai (WA), giúp bạn phát hiện bug logic trong chớp mắt.

---

## 8.3. Tạo Bộ sinh Test Ngẫu nhiên & Stress Testing

Khi nộp bài bị **Wrong Answer (WA)** trên một test bí mật mà bạn không biết test đó là gì, **Stress Testing** là vũ khí mạnh nhất để tìm ra test sai trong vòng 3 phút!

### Kiến trúc hệ thống Stress Testing gồm 4 file:
1. `sol.cpp`: Thuật toán tối ưu của bạn (đang bị WA).
2. `brute.cpp`: Thuật toán Brute Force ngây thơ (chắc chắn đúng 100% nhưng chạy chậm).
3. `gen.cpp`: Chương trình sinh test ngẫu nhiên theo đúng format và constraints nhỏ ($N \le 10, A_i \le 20$).
4. `stress.bat` (trên Windows Powershell/CMD) tự động chạy lặp cho đến khi hai file cho kết quả khác nhau:

```powershell
# Script Stress Test trên Windows PowerShell:
$i = 1
while ($true) {
    ./gen > input.txt
    ./sol < input.txt > out1.txt
    ./brute < input.txt > out2.txt
    $diff = Compare-Object (Get-Content out1.txt) (Get-Content out2.txt)
    if ($diff) {
        Write-Host "FOUND MISMATCH AT TEST $i !" -ForegroundColor Red
        Get-Content input.txt
        break
    }
    Write-Host "Passed test $i" -ForegroundColor Green
    $i++
}
```

---

## 8.4. Chiến thuật ICPC đồng đội (3 người - 1 máy tính)

### 1. Phân bổ vai trò trong đội
- **Thành viên A (Speed Demon / Implementation Specialist):** Người có kỹ năng gõ code nhanh nhất, ít lỗi cú pháp nhất. Chuyên nhận nhiệm vụ code các bài dễ và các bài đã có thuật toán rõ ràng từ 2 thành viên còn lại.
- **Thành viên B (Math & Hard Thinker):** Chuyên sâu về Toán học, Quy hoạch động khó, và các bài toán Ad-hoc/Constructive. Ngồi nháp trên giấy và chứng minh thuật toán.
- **Thành viên C (Data Structures & Graph Specialist / Verifier):** Chuyên về cấu trúc dữ liệu nặng, kiểm tra góc khuất (Edge cases), viết generator và stress test khi bài bị WA.

### 2. Quy tắc Bàn phím Vàng (Golden Keyboard Rule)
- **Không bao giờ ngồi ôm bàn phím để suy nghĩ:** Bàn phím là tài nguyên hữu hạn duy nhất của đội. Nếu chưa có thuật toán chi tiết và các trường hợp biên trên giấy, phải nhường máy cho người khác code.
- **Nếu nộp bài bị WA:** LẬP TỨC in code ra giấy (hoặc chép ra nháp), rời khỏi bàn phím cho đồng đội vào làm bài khác. Đọc lại code trên giấy để tìm bug logic. 90% lỗi sai được tìm thấy nhanh hơn khi đọc trên giấy!

---
---

# CHƯƠNG 9: PATTERN RECOGNITION (BẢNG TRA CỨU NHẬN DIỆN MÔ HÌNH THUẬT TOÁN)

> *"Đừng học thuộc code. Hãy ghi nhớ hình thái cấu trúc của bài toán."*

Chương này cung cấp ma trận nhận diện mô hình bài toán toàn diện nhất, giúp bạn định hướng thuật toán chính xác chỉ trong 60 giây sau khi đọc đề.

---

## 9.1. Ma trận nhận diện theo Constraints & Dấu hiệu bài toán

| Dấu hiệu đề bài | Cấu trúc dữ liệu đầu vào | Constraints | Hướng suy nghĩ ban đầu | Thuật toán ứng cử viên | Điều kiện lựa chọn chính xác |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Tìm giá trị lớn nhất của giá trị nhỏ nhất (hoặc ngược lại) | Mảng số nguyên | $N \le 2 \cdot 10^5$, Giá trị $\le 10^9$ | Kiểm tra tính đơn điệu của hàm điều kiện | **Binary Search on Answer** | Nếu biết nghiệm $X$, việc kiểm tra xem có đạt được $X$ hay không làm được trong $O(N)$ |
| Đếm số đoạn con liên tiếp có tổng $\le K$ (hoặc chứa $\le K$ phần tử phân biệt) | Mảng số không âm | $N \le 10^6$ | Cửa sổ trượt có tính chất co giãn bảo toàn điều kiện | **Two Pointers / Sliding Window** | Mọi phần tử đều $\ge 0$ (tổng tăng đơn điệu khi mở rộng $R$). Nếu có số âm $\implies$ chuyển sang Prefix Sum + Fenwick/Map |
| Tìm chuỗi thao tác ít nhất để biến trạng thái $A$ thành $B$ | Trạng thái lưới hoặc số | Số trạng thái $\le 10^6$, chi phí mỗi bước = 1 | Đồ thị hóa không gian trạng thái | **BFS (Breadth-First Search)** | Mỗi thao tác có trọng số bằng 1. Nếu có trọng số 0 và 1 $\implies$ Dùng **0-1 BFS**. Nếu trọng số dương bất kỳ $\implies$ **Dijkstra** |
| Cho tập hợp các công việc có thời gian bắt đầu và kết thúc | Danh sách đoạn $[L_i, R_i]$ | $N \le 2 \cdot 10^5$ | Sắp xếp theo một đầu mút để tham lam | **Greedy theo thời gian kết thúc sớm nhất** | Các công việc có giá trị bằng nhau. Nếu mỗi công việc có một trọng số giá trị khác nhau $\implies$ **DP + Chặt nhị phân** |
| Truy vấn cập nhật đoạn và tính tổng/min/max trên đoạn | Mảng $N$ phần tử | $N, Q \le 2 \cdot 10^5$ | Quản lý khoảng phân cấp | **Segment Tree với Lazy Propagation** | Thao tác cập nhật có tính chất kết hợp (Associative). Nếu chỉ cập nhật điểm $\implies$ Dùng **Fenwick Tree** cho nhẹ |
| Đồ thị có điều kiện logic: "Nếu chọn A thì phải chọn B", "Không thể chọn cả A và B" | Tập các mệnh đề nhị phân | $N \le 2 \cdot 10^5$ | Đồ thị suy diễn mũi tên $\implies$ | **2-SAT (Tarjan SCC)** | Mỗi mệnh đề chỉ chứa tối đa 2 biến logic. Nếu mệnh đề có từ 3 biến trở lên $\implies$ NP-Complete! |
| Đếm số lượng cấu hình / Tìm cách sắp xếp tối ưu | $N$ phần tử | $N \le 20$ | Biểu diễn tập con bằng bit | **Bitmask DP** | Trạng thái tiếp theo chỉ phụ thuộc vào tập hợp các phần tử đã được chọn, không phụ thuộc thứ tự cụ thể |
| Đếm số trong khoảng $[A, B]$ thỏa mãn tính chất chữ số | Hai số $A, B \le 10^{18}$ | Độ dài số $\le 18$ | Xây dựng từng chữ số từ trái sang phải | **Digit DP** | Độc lập giữa các chữ số hoặc chỉ phụ thuộc vào chữ số liền trước / tổng chữ số |

---

## 9.2. Phân tích đối chiếu các cặp bài toán dễ gây nhầm lẫn

### Cặp đối chiếu 1: Cùng tìm cách đổi tiền nhưng 2 bài toán hoàn toàn khác nhau!
- **Bài toán A (Coin Change - Greedy):** Hệ thống tiền tệ là tiền xu chuẩn của một quốc gia $\{1, 2, 5, 10, 20, 50, 100\}$. Tìm số lượng đồng xu ít nhất để đổi số tiền $S$.
  - $\implies$ **Giải bằng THAM LAM (Greedy):** Luôn chọn đồng xu có mệnh giá lớn nhất có thể. Đúng vì hệ thống tiền tệ là hệ thống chính quy (Canonical Coin System), mệnh giá sau luôn là bội số hoặc kết hợp tối ưu của mệnh giá trước.
- **Bài toán B (Coin Change - General DP):** Cho các đồng xu có mệnh giá kỳ dị bất kỳ $\{1, 6, 10\}$. Đổi số tiền $S = 12$.
  - Nếu dùng Greedy: Chọn $10 \to$ còn lại 2 đồng $1 \implies$ Tổng cộng mất 3 đồng xu $(10 + 1 + 1)$.
  - Nghiệm tối ưu thực tế: $6 + 6 = 12 \implies$ Chỉ mất đúng 2 đồng xu!
  - $\implies$ **BẮT BUỘC DÙNG QUY HOẠCH ĐỘNG (DP):** $dp[i] = 1 + \min(dp[i - c])$.

### Cặp đối chiếu 2: Đoạn con liên tiếp có tổng bằng $S$
- **Trường hợp A: Mảng toàn số nguyên DƯƠNG ($A_i > 0$).**
  - $\implies$ **Giải bằng TWO POINTERS trong $O(N)$ thời gian, $O(1)$ bộ nhớ:** Vì toàn số dương nên tổng tăng đơn điệu khi mở rộng $R$, giảm khi thu hẹp $L$.
- **Trường hợp B: Mảng có cả số nguyên ÂM ($A_i \in [-10^9, 10^9]$).**
  - Tính đơn điệu bị phá vỡ hoàn toàn! Mở rộng $R$ tổng có thể giảm, thu hẹp $L$ tổng có thể tăng $\implies$ Two Pointers sai 100%!
  - $\implies$ **BẮT BUỘC DÙNG PREFIX SUM + HASH MAP / SAFE MAP trong $O(N)$:**
    $$Prefix[R] - Prefix[L-1] = S \iff Prefix[L-1] = Prefix[R] - S$$
    Duyệt $R$ và đếm số lượng tiền tố bằng $Prefix[R] - S$ đã xuất hiện trong Map.

### Cặp đối chiếu 3: Tìm đường đi ngắn nhất trên lưới ô vuông
- **Trường hợp A: Chi phí đi qua mỗi ô là 1 bước.**
  - $\implies$ Dùng **BFS ngây thơ** với hàng đợi `std::queue` trong $O(R \times C)$. Tuyệt đối không dùng Dijkstra vì Dijkstra sẽ tốn thêm thừa số $O(\log(RC))$ và hằng số của Heap!
- **Trường hợp B: Đi thẳng chi phí 0, rẽ hướng chi phí 1.**
  - $\implies$ Dùng **0-1 BFS** với `std::deque` trong $O(R \times C)$.
- **Trường hợp C: Mỗi ô có một độ cao/chi phí bùn lầy bất kỳ $W_{r,c} \ge 0$.**
  - $\implies$ Bắt buộc dùng **Dijkstra** với `std::priority_queue` trong $O(RC \log(RC))$.

---
# CHƯƠNG 10: ONLINE JUDGE PRACTICE (NGÂN HÀNG BÀI TẬP THỰC TẾ ĐÃ XÁC MINH)

> *"Không giải bài để tích lũy số lượng. Giải bài để tích lũy mẫu tư duy."*

Tất cả các bài tập dưới đây đều được tuyển chọn kỹ lưỡng từ các kỳ thi chính thức, có đường dẫn trực tiếp đang hoạt động (verified), phân cấp từ cơ bản đến nâng cao.

---

## 10.1. Level 1: Fundamental (Xây dựng nền tảng tư duy)

### 1. [CSES - Static Range Sum Queries](https://cses.fi/problemset/task/1646)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Introductory / 800 - 900
- **Chủ đề:** Mảng cộng dồn (Prefix Sums)
- **Kỹ năng tư duy:** Nhận diện việc tiền xử lý $O(N)$ để trả lời truy vấn đoạn tĩnh trong $O(1)$.
- **Mục tiêu:** Cài đặt 1-based indexing không lỗi tràn số (`long long`).

### 2. [CSES - Subarray Sums I](https://cses.fi/problemset/task/1660)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Sorting & Searching / 1100
- **Chủ đề:** Two Pointers / Sliding Window
- **Kỹ năng tư duy:** Khai thác tính đơn điệu của mảng số nguyên dương ($A_i > 0$).
- **Mục tiêu:** Tự chứng minh con trỏ $L$ và $R$ chỉ dịch chuyển tối đa $N$ lần, đảm bảo độ phức tạp $O(N)$.

### 3. [CSES - Maximum Subarray Sum](https://cses.fi/problemset/task/1643)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Sorting & Searching / 1000
- **Chủ đề:** Dynamic Programming / Thuật toán Kadane
- **Kỹ năng tư duy:** Phân rã bài toán: Đoạn con tốt nhất kết thúc tại $i$ hoặc là chỉ gồm chính nó, hoặc là ghép nối với đoạn tốt nhất kết thúc tại $i-1$.
- **Mục tiêu:** Cài đặt $O(N)$ thời gian, $O(1)$ bộ nhớ, xử lý trơn tru trường hợp toàn mảng là số âm.

### 4. [CSES - Counting Rooms](https://cses.fi/problemset/task/1192)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Graph Algorithms / 1000
- **Chủ đề:** BFS / DFS trên lưới ô vuông
- **Kỹ năng tư duy:** Biến đổi bảng 2D thành đồ thị liên thông không trọng số.
- **Mục tiêu:** Thành thạo mảng hướng dịch chuyển `const int dx[] = {-1, 1, 0, 0}; const int dy[] = {0, 0, -1, 1};`.

### 5. [AtCoder DP Contest - Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a)
- **Nền tảng:** AtCoder Educational DP Contest
- **Rating / Độ khó:** AtCoder 400 / CF 900
- **Chủ đề:** Quy hoạch động cơ bản 1 chiều
- **Kỹ năng tư duy:** Thiết lập phương trình trạng thái và xác định Base Case.
- **Mục tiêu:** Cài đặt thành thạo cả 2 phong cách Pull DP và Push DP.

### 6. [CSES - Exponentiation](https://cses.fi/problemset/task/1095)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Mathematics / 900
- **Chủ đề:** Lũy thừa nhị phân (Binary Exponentiation)
- **Kỹ năng tư duy:** Phân tích bit của số mũ để giảm số phép nhân từ $O(B)$ xuống $O(\log B)$.
- **Mục tiêu:** Viết hàm `powerMod` chuẩn mực không bị tràn số `__int128` hoặc `long long`.

---

## 10.2. Level 2: Intermediate (Kỳ thi tháng 12/2026 & ICPC National)

### 1. [CSES - Factory Machines](https://cses.fi/problemset/task/1620)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Sorting & Searching / 1200
- **Chủ đề:** Chặt nhị phân trên kết quả (Binary Search on Answer)
- **Kỹ năng tư duy:** Nhận diện tính đơn điệu: Thời gian càng nhiều thì số sản phẩm làm được càng tăng.
- **Mục tiêu:** Tránh tràn số khi tính $\sum \lfloor mid / k_i \rfloor$ bằng cách dừng sớm khi tổng $\ge T$.

### 2. [Codeforces 1201C - Maximum Median](https://codeforces.com/problemset/problem/1201/C)
- **Nền tảng:** Codeforces
- **Rating / Độ khó:** 1400
- **Chủ đề:** Sắp xếp + Chặt nhị phân trên kết quả
- **Kỹ năng tư duy:** Nhận diện phần tử trung vị chỉ bị ảnh hưởng bởi nửa sau của mảng sau khi đã sắp xếp.
- **Mục tiêu:** Viết hàm kiểm tra $O(N)$ độc lập với thuật toán nhị phân bên ngoài.

### 3. [CSES - Dynamic Range Minimum Queries](https://cses.fi/problemset/task/1649)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Range Queries / 1300
- **Chủ đề:** Segment Tree (Point Update, Range Query)
- **Kỹ năng tư duy:** Phân chia khoảng đệ quy nhị phân.
- **Mục tiêu:** Tự code Segment Tree không nhìn tài liệu trong vòng 5 phút.

### 4. [CSES - Shortest Routes I](https://cses.fi/problemset/task/1671)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Graph Algorithms / 1200
- **Chủ đề:** Thuật toán Dijkstra
- **Kỹ năng tư duy:** Chứng minh việc lấy đỉnh có khoảng cách nhỏ nhất trong `priority_queue` đảm bảo tính tối ưu cục bộ không bị đảo ngược.
- **Mục tiêu:** Sử dụng `dist[u] < d` để bỏ qua các bản sao cũ trong heap.

### 5. [CSES - Course Schedule](https://cses.fi/problemset/task/1679)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Graph Algorithms / 1200
- **Chủ đề:** Topological Sort / Thuật toán Kahn
- **Kỹ năng tư duy:** Mô hình hóa điều kiện tiên quyết thành đồ thị có hướng và phát hiện chu trình.
- **Mục tiêu:** Cài đặt hàng đợi In-degree chuẩn mực.

### 6. [Codeforces 230B - T-primes](https://codeforces.com/problemset/problem/230/B)
- **Nền tảng:** Codeforces
- **Rating / Độ khó:** 1300
- **Chủ đề:** Sàng số nguyên tố + Nhận xét Toán học
- **Kỹ năng tư duy:** Chứng minh một số có đúng 3 ước số dương khi và chỉ khi nó là bình phương của một số nguyên tố.
- **Mục tiêu:** Kết hợp sàng Eratosthenes đến $10^6$ với hàm căn bậc hai số học chính xác.

### 7. [AtCoder DP Contest - Knapsack 2](https://atcoder.jp/contests/dp/tasks/dp_e)
- **Nền tảng:** AtCoder Educational DP Contest
- **Rating / Độ khó:** AtCoder 500 / CF 1500
- **Chủ đề:** Quy hoạch động đảo trạng thái (State Flipping DP)
- **Kỹ năng tư duy:** Khi sức chứa balo $W \le 10^9$ quá lớn, đảo vai trò: $dp[v]$ là trọng lượng nhỏ nhất để đạt được tổng giá trị đúng bằng $v$.
- **Mục tiêu:** Nắm vững kỹ thuật đảo chiều biến số mục tiêu khi Constraints thay đổi.

---

## 10.3. Level 3: Advanced / ICPC (Chinh phục ICPC Regional & 2027)

### 1. [CSES - Elevator Rides](https://cses.fi/problemset/task/1653)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES DP / 1600
- **Chủ đề:** Bitmask DP + Tham lam kết hợp
- **Kỹ năng tư duy:** Thiết kế cặp trạng thái $(rides, last\_weight)$ tối ưu hóa đồng thời số chuyến và khối lượng chuyến cuối.
- **Mục tiêu:** Duyệt $2^N$ mặt nạ bit trong $O(N \cdot 2^N)$.

### 2. [CSES - Counting Numbers](https://cses.fi/problemset/task/2220)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES DP / 1700
- **Chủ đề:** Digit DP (Quy hoạch động chữ số)
- **Kỹ năng tư duy:** Phân tách bài toán theo nguyên lý tiền tố $f(B) - f(A-1)$ và duy trì trạng thái chữ số liền trước.
- **Mục tiêu:** Xử lý triệt để cờ `tight` và cờ `leading_zero`.

### 3. [CSES - Distinct Routes](https://cses.fi/problemset/task/1711)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Advanced Graph / 1800
- **Chủ đề:** Luồng cực đại (Max Flow - Thuật toán Dinic) + Phục hồi đường đi
- **Kỹ năng tư duy:** Quy giảm bài toán tìm tập đường đi không chung cạnh về bài toán tìm luồng trên mạng dung lượng đơn vị.
- **Mục tiêu:** Phục hồi các đường đi độc lập từ dòng luồng dư thừa bằng DFS.

### 4. [CSES - Giant Pizza](https://cses.fi/problemset/task/1684)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Advanced Graph / 1600
- **Chủ đề:** 2-Satisfiability (2-SAT)
- **Kỹ năng tư duy:** Dựng đồ thị suy diễn 2 cạnh cho mỗi mệnh đề logic và kiểm tra điều kiện liên thông mạnh với Tarjan.
- **Mục tiêu:** Gán giá trị Boolean cho các biến theo thứ tự tô-pô ngược của các SCC.

### 5. [Codeforces 52C - Circular RMQ](https://codeforces.com/problemset/problem/52/C)
- **Nền tảng:** Codeforces
- **Rating / Độ khó:** 2200
- **Chủ đề:** Segment Tree với Lazy Propagation trên mảng vòng tròn
- **Kỹ năng tư duy:** Tách đoạn vòng tròn $[L, R]$ với $L > R$ thành hai truy vấn đoạn liên tiếp độc lập $[L, N-1]$ và $[0, R]$.
- **Mục tiêu:** Cài đặt Lazy Update không bug và parse chuỗi dòng lệnh linh hoạt.

### 6. [CSES - Tree Distances II](https://cses.fi/problemset/task/1133)
- **Nền tảng:** CSES Problem Set
- **Rating / Độ khó:** CSES Tree Algorithms / 1500
- **Chủ đề:** Rerooting DP (Quy hoạch động đổi gốc cây)
- **Kỹ năng tư duy:** Tính toán sự chênh lệch khoảng cách khi di chuyển gốc từ nút cha sang nút con: $\Delta = (N - sz[v]) - sz[v]$.
- **Mục tiêu:** Cài đặt 2 lượt DFS giải quyết bài toán trong $O(N)$ thay vì $O(N^2)$.

---
---

# CHƯƠNG 11: TRAINING ROADMAP (LỘ TRÌNH HUẤN LUYỆN 11/2026 - ICPC 2027)

Lộ trình được thiết kế chi tiết theo 5 giai đoạn chiến lược, bảo đảm cân bằng giữa học lý thuyết, cài đặt thuật toán và áp lực phòng thi.

```
+-----------------------------------------------------------------------------------------+
|                                    TỔNG QUAN LỘ TRÌNH                                   |
|                                                                                         |
|  Phase 1: Nước rút kỳ thi 12/2026 (11/2026 - 12/2026) -> 6 tuần: Củng cố lõi & Tốc độ  |
|  Phase 2: Nền tảng Toán & Thuật toán lõi (01/2027 - 03/2027) -> 12 tuần: Chắc bản chất  |
|  Phase 3: Cấu trúc nâng cao & Đồ thị lớn (04/2027 - 07/2027) -> 16 tuần: Bứt phá đỉnh cao|
|  Phase 4: Luyện đề ICPC Regional (08/2027 - 09/2027) -> 8 tuần: Phối hợp đội tuyển     |
|  Phase 5: Contest Simulation & Peak (10/2027 - 11/2027) -> 6 tuần: Đỉnh cao phong độ   |
+-----------------------------------------------------------------------------------------+
```

---

## 11.1. Phase 1: Nước rút kỳ thi tháng 12/2026 (6 tuần)

- **Mục tiêu tối thượng:** Đạt điểm tuyệt đối các bài cơ bản/trung bình, không mắc lỗi ngớ ngẩn (overflow, off-by-one, TLE do dùng cin/cout chậm), thành thạo toàn bộ Cấu trúc dữ liệu và Quy hoạch động cơ bản.

### Tuần 1: Master Two Pointers, Binary Search & Prefix Sums
- **Kiến thức:** Monotonicity predicate, 1D/2D Prefix Sums, Difference Array, Binary Search on Answer.
- **Mục tiêu:** Code xong các bài dưới 1200 trong vòng 10 phút/bài.
- **Bài tập mục tiêu (5 bài):**
  1. [CSES - Static Range Sum Queries](https://cses.fi/problemset/task/1646)
  2. [CSES - Subarray Sums I](https://cses.fi/problemset/task/1660)
  3. [CSES - Subarray Sums II](https://cses.fi/problemset/task/1661)
  4. [CSES - Factory Machines](https://cses.fi/problemset/task/1620)
  5. [Codeforces 1201C - Maximum Median](https://codeforces.com/problemset/problem/1201/C)
- **Kiểm tra cuối tuần:** Virtual Contest Codeforces Div 3 (Giải quyết bài A, B, C, D trong 60 phút).

### Tuần 2: Cấu trúc dữ liệu tuyến tính & Fenwick Tree
- **Kiến thức:** Monotonic Stack, Monotonic Queue, Disjoint Set Union (DSU), Fenwick Tree (Point Add Range Sum).
- **Mục tiêu:** Nắm vững cấu trúc Fenwick Tree, không nhầm lẫn phép bit `i += i & (-i)`.
- **Bài tập mục tiêu (5 bài):**
  1. [CSES - Nearest Smaller Values](https://cses.fi/problemset/task/1645)
  2. [CSES - Road Construction](https://cses.fi/problemset/task/1676)
  3. [CSES - Dynamic Range Sum Queries](https://cses.fi/problemset/task/1648)
  4. [Codeforces 547B - Mike and Feet](https://codeforces.com/problemset/problem/547/B)
  5. [VNOI - NKINV](https://oj.vnoi.info/problem/nkinv)
- **Kiểm tra cuối tuần:** Giải bài tập Fenwick Tree 2D tính tổng vùng hình chữ nhật trong 45 phút.

### Tuần 3: Quy hoạch động 1D & 2D cổ điển
- **Kiến thức:** Đổi tiền (Coin Change), Dãy con tăng dài nhất ($O(N \log N)$), Knapsack 0/1, Knapsack vô hạn, LCS, Edit Distance.
- **Mục tiêu:** Nhận diện ngay trạng thái bài toán Knapsack, tối ưu bộ nhớ từ 2 chiều về 1 chiều.
- **Bài tập mục tiêu (5 bài):**
  1. [CSES - Coin Combinations I](https://cses.fi/problemset/task/1635)
  2. [CSES - Coin Combinations II](https://cses.fi/problemset/task/1636)
  3. [CSES - Book Shop](https://cses.fi/problemset/task/1158)
  4. [CSES - Increasing Subsequence](https://cses.fi/problemset/task/1145)
  5. [CSES - Edit Distance](https://cses.fi/problemset/task/1639)
- **Kiểm tra cuối tuần:** Làm 4 bài đầu tiên của AtCoder Educational DP Contest trong 60 phút.

### Tuần 4: Đồ thị cơ bản (BFS, DFS, Dijkstra, Kruskal)
- **Kiến thức:** Đồ thị dạng lưới, kiểm tra 2 phía (Bipartite Graph), Dijkstra với heap, Cây khung nhỏ nhất Kruskal với DSU.
- **Mục tiêu:** Viết Dijkstra không bug trong 7 phút.
- **Bài tập mục tiêu (5 bài):**
  1. [CSES - Building Roads](https://cses.fi/problemset/task/1666)
  2. [CSES - Message Route](https://cses.fi/problemset/task/1667)
  3. [CSES - Shortest Routes I](https://cses.fi/problemset/task/1671)
  4. [CSES - Road Reparation](https://cses.fi/problemset/task/1675)
  5. [Codeforces 20C - Dijkstra?](https://codeforces.com/problemset/problem/20/C)
- **Kiểm tra cuối tuần:** Giải bài toán mê cung kết hợp trạng thái phụ (BFS trên đồ thị trạng thái).

### Tuần 5: Thuật toán Cây & Segment Tree cơ bản
- **Kiến thức:** Đường kính cây, Binary Lifting tìm LCA, Segment Tree đơn giản (Point Update, Range Query).
- **Mục tiêu:** Cài đặt Segment Tree không đệ quy hoặc đệ quy chuẩn mực.
- **Bài tập mục tiêu (5 bài):**
  1. [CSES - Tree Diameter](https://cses.fi/problemset/task/1131)
  2. [CSES - Company Queries I](https://cses.fi/problemset/task/1687)
  3. [CSES - Company Queries II](https://cses.fi/problemset/task/1688)
  4. [CSES - Dynamic Range Minimum Queries](https://cses.fi/problemset/task/1649)
  5. [Codeforces 339D - Xenia and Bit Operations](https://codeforces.com/problemset/problem/339/D)
- **Kiểm tra cuối tuần:** Mô phỏng kỳ thi 3 tiếng (3 bài tập tổng hợp).

### Tuần 6: Chiến thuật phòng thi, Stress Testing & Tổng duyệt
- **Kiến thức:** Thiết lập hệ thống Stress Testing tự động, các bẫy tràn số `long long`, corner case $N=1$.
- **Mục tiêu:** Tự tin 100% bước vào kỳ thi tháng 12/2026.
- **Hoạt động:** Chạy 2 Contest thử nghiệm đầy đủ thời gian thực, rèn luyện thói quen viết `assert` và kiểm tra constraints.

---

## 11.2. Phase 2: Củng cố nền tảng Toán học & Thuật toán lõi (01/2027 - 03/2027)

- **Mục tiêu:** Thành thạo Number Theory chuyên sâu, Combinatorics, Sàng tuyến tính, Suffix/Prefix tricks, Bitmask DP, Tree DP.
- **Phân bổ 12 tuần:**
  - **Tuần 7-9:** Số học chuyên sâu (Nghịch đảo modulo, Euclid mở rộng, nguyên lý Dirichlet, nguyên lý bù trừ PIE).
  - **Tuần 10-12:** Đại số tổ hợp (Catalan, Stars and Bars, Lucas Theorem, nhị thức Newton).
  - **Tuần 13-15:** Bitmask DP chuyên sâu và Quy hoạch động chữ số (Digit DP).
  - **Tuần 16-18:** Tree DP, Kỹ thuật đổi gốc (Rerooting DP), Euler Tour kết hợp Segment Tree.

---

## 11.3. Phase 3: Nâng cấp Cấu trúc dữ liệu & Thuật toán nâng cao (04/2027 - 07/2027)

- **Mục tiêu:** Đạt trình độ giải quyết các bài Division 1 / ICPC National & Regional khó.
- **Nội dung trọng điểm:**
  - Segment Tree với Lazy Propagation phức tạp.
  - Persistent Segment Tree (Range K-th query).
  - Thuật toán xâu: String Hashing an toàn, KMP, Z-algorithm, Aho-Corasick.
  - Đồ thị nâng cao: Thành phần liên thông mạnh (Tarjan SCC), 2-SAT, Luồng cực đại (Dinic).
  - Phân rã cây: Heavy-Light Decomposition (HLD) và Centroid Decomposition.
  - Thuật toán Mo và Chia căn (Square Root Decomposition).

---

## 11.4. Phase 4: Luyện đề ICPC Regional & Phối hợp đội tuyển (08/2027 - 09/2027)

- **Mục tiêu:** Đồng bộ hóa kỹ năng làm việc nhóm 3 người - 1 máy tính.
- **Nội dung:**
  - Mỗi tuần luyện tập **2 bộ đề ICPC Regional các năm trước** (thời gian thực 5 tiếng/contest).
  - Rèn luyện kỹ thuật phân công: Người đọc đề, người nháp toán, người gõ code.
  - Tối ưu hóa cuốn **ICPC Team Notebook (25 trang in code template)**.

---

## 11.5. Phase 5: Contest Simulation & Đạt điểm rơi phong độ (10/2027 - 11/2027)

- **Mục tiêu:** Tinh thần thép, không bị hoảng loạn khi bài đầu tiên bị bế tắc, đạt trạng thái thi đấu đỉnh cao tại kỳ thi ICPC 2027.
- **Nội dung:** Giảm cường độ học thuật toán mới, tập trung tối đa vào việc làm bài không bug, phân tích lỗi sai trong quá khứ và rèn luyện thể lực, nhịp sinh học chuẩn bị cho ngày thi đấu chính thức.

---
---

# CHƯƠNG 12: PROBLEM ANALYSIS TEMPLATE (KHUNG PHÂN TÍCH BÀI TOÁN CHUẨN MỰC)

> *"Một bài toán được phân tích đúng phương pháp đã được giải quyết một nửa trước khi viết dòng code đầu tiên."*

Mỗi khi gặp một bài toán thuật toán từ mức trung bình trở lên, hãy tuân thủ nghiêm ngặt khung phân tích 13 bước chuẩn mực dưới đây:

---

## 12.1. Quy trình 13 bước chuẩn mực

```
1. Problem Summary: Tóm tắt đề bài thành 1-2 câu toán học thuần túy.
2. Constraints Analysis: Phân tích N, M, Time, Memory để khóa giới hạn độ phức tạp.
3. Brute Force Approach: Xây dựng giải pháp vét cạn ngây thơ ban đầu.
4. Bottleneck Identification: Chỉ rõ vòng lặp hoặc thao tác nào làm giải pháp bị chậm.
5. Key Observations: Các quan sát then chốt rút ra từ ví dụ nhỏ trên giấy.
6. Mathematical Properties: Tính chất đơn điệu, bất biến, tính chẵn lẻ hoặc đẳng thức.
7. Optimized Approach: Đề xuất thuật toán tối ưu giải quyết nút thắt cổ chai.
8. Correctness Proof: Chứng minh tính đúng đắn (Quy nạp, Phản chứng, Exchange Argument).
9. Complexity Analysis: Đánh giá Big-O chính xác về Thời gian và Bộ nhớ.
10. Implementation: Viết code C++17/20 sạch sẽ, chuẩn mực, tối ưu hóa I/O.
11. Edge Cases: Kiểm tra các trường hợp biên cực đoan (N=1, mảng âm, số tràn).
12. Alternative Approaches: Xem xét các cách giải khác (nếu có).
13. Lessons Learned: Rút ra mẫu bài toán (Pattern) để tái sử dụng trong tương lai.
```

---

## 12.2. Ví dụ thực hành phân tích hoàn chỉnh

### Đề bài mẫu: [CSES - Projects](https://cses.fi/problemset/task/1140)
*Có $N$ dự án. Mỗi dự án diễn ra từ ngày $A_i$ đến ngày $B_i$ và mang lại phần thưởng $P_i$. Hai dự án không được giao nhau về thời gian (nếu chọn dự án kết thúc tại $B_i$, dự án tiếp theo phải bắt đầu từ ngày $\ge B_i + 1$). Hãy tìm tổng phần thưởng lớn nhất có thể đạt được.*

#### Bước 1: Problem Summary
Tìm tập hợp các đoạn không giao nhau $[A_i, B_i]$ sao cho tổng trọng số $\sum P_i$ là lớn nhất.

#### Bước 2: Constraints Analysis
- $N \le 2 \cdot 10^5$.
- $1 \le A_i \le B_i \le 10^9$.
- $1 \le P_i \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 512MB.
- $\implies$ Độ phức tạp thời gian mục tiêu bắt buộc phải là **$O(N \log N)$**. Không thể dùng mảng kích thước $10^9$ theo thời gian.

#### Bước 3: Brute Force Approach
Với mỗi dự án, ta có 2 lựa chọn: Chọn hoặc Bỏ qua. Dùng đệ quy quay lui sinh toàn bộ $2^N$ cấu hình, kiểm tra các đoạn có giao nhau không $\implies O(N \cdot 2^N)$. Quá thời gian trầm trọng.

#### Bước 4: Bottleneck Identification
Nút thắt của Brute Force: Với mỗi dự án được chọn, ta phải duyệt lại toàn bộ các dự án trước đó để tìm dự án kết thúc trước $A_i$ mang lại tổng thưởng cao nhất.

#### Bước 5: Key Observations
1. Quyết định chọn dự án thứ $i$ chỉ phụ thuộc vào thời điểm kết thúc của các dự án trước đó.
2. Nếu ta sắp xếp các dự án theo **thời gian kết thúc $B_i$ tăng dần**, khi xét tới dự án $i$, mọi dự án đã xử lý đều kết thúc trước hoặc cùng lúc với $i$.

#### Bước 6: Mathematical Properties
Bài toán thỏa mãn tính chất con tối ưu (Optimal Substructure):
Giá trị lớn nhất có thể đạt được sau khi xét $i$ dự án đầu tiên là:
$$dp[i] = \max(dp[i - 1], P_i + dp[k])$$
Trong đó $k$ là dự án có thời gian kết thúc $B_k < A_i$ lớn nhất có thể.

#### Bước 7: Optimized Approach
- Sắp xếp mảng dự án theo $B_i$ tăng dần.
- Dùng Chặt nhị phân (`std::lower_bound` hoặc hàm tự viết) trên danh sách $B$ để tìm chỉ số $k$ trong thời gian $O(\log N)$.
- Duy trì mảng $dp[i]$ là kết quả tối ưu của $i$ dự án đầu tiên.

#### Bước 8: Correctness Proof
- **Quy nạp toán học:** 
  - Với $i = 1$, $dp[1] = P_1$ (chính xác).
  - Giả sử $dp[1..i-1]$ đã lưu nghiệm tối ưu của các bài toán con tương ứng.
  - Tại bước $i$, nghiệm tối ưu chỉ có 2 khả năng: Hoặc không chọn dự án $i$ (kết quả là $dp[i-1]$), hoặc chọn dự án $i$ (khi đó không thể chọn bất kỳ dự án nào kết thúc sau $A_i - 1$, nên phương án tốt nhất đi kèm bắt buộc phải là $dp[k]$ với $B_k < A_i$). Lấy $\max$ giữa 2 khả năng chắc chắn cho nghiệm tối ưu toàn cục.

#### Bước 9: Complexity Analysis
- Sắp xếp: $O(N \log N)$.
- Vòng lặp $N$ bước, mỗi bước chặt nhị phân $O(\log N)$: $O(N \log N)$.
- Bộ nhớ: $O(N)$ lưu mảng dự án và mảng DP.
- Hoàn toàn thỏa mãn giới hạn $N = 2 \cdot 10^5$ trong 0.2 giây!

#### Bước 10: Implementation (C++20 Clean Code)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Project {
    int start, end, reward;
    bool operator<(const Project& other) const {
        return end < other.end;
    }
};

int main() {
    // Tối ưu hóa I/O
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    if (!(std::cin >> n)) return 0;

    std::vector<Project> p(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> p[i].start >> p[i].end >> p[i].reward;
    }

    // 1. Sắp xếp theo ngày kết thúc tăng dần
    std::sort(p.begin(), p.end());

    // Mảng lưu thời điểm kết thúc để chặt nhị phân
    std::vector<int> end_times(n);
    for (int i = 0; i < n; ++i) {
        end_times[i] = p[i].end;
    }

    // dp[i] là lợi nhuận lớn nhất xét đến dự án i (1-based)
    std::vector<long long> dp(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        // Trường hợp 1: Không chọn dự án i
        long long op1 = dp[i - 1];

        // Trường hợp 2: Chọn dự án i
        // Tìm dự án k xa nhất có end < p[i-1].start
        auto it = std::lower_bound(end_times.begin(), end_times.end(), p[i - 1].start);
        int k = std::distance(end_times.begin(), it); // số lượng dự án có end < start

        long long op2 = p[i - 1].reward + dp[k];

        dp[i] = std::max(op1, op2);
    }

    std::cout << dp[n] << "\n";
    return 0;
}
```

#### Bước 11: Edge Cases
- $N = 1$: Chạy đúng, trả về $P_1$.
- Các dự án gối sát mép nhau ($A_j = B_i$): Đề bài quy định thời gian không giao nhau, tức là nếu dự án kết thúc tại ngày $X$, dự án sau bắt đầu từ ngày $X$ là vi phạm. Thuật toán dùng `lower_bound` tìm vị trí đầu tiên $\ge A_j$, tức là các dự án được chọn đều có $B_k < A_j$ $\implies$ Xử lý chính xác 100%.
- Tổng thưởng vượt $2 \cdot 10^9$: Mảng `dp` dùng kiểu `long long` $\implies$ Tránh hoàn toàn tràn số nguyên 32-bit.

#### Bước 12: Alternative Approaches
Có thể rời rạc hóa tọa độ thời gian (Coordinate Compression) kết hợp Segment Tree / Fenwick Tree để cập nhật điểm và truy vấn max trên đoạn $[1, A_i - 1]$. Tuy nhiên cách dùng DP + Binary Search đơn giản và chạy nhanh hơn nhiều.

#### Bước 13: Lessons Learned
Mô hình **Weighted Interval Scheduling** luôn được giải tối ưu bằng cách: Sắp xếp theo thời điểm kết thúc + Quy hoạch động 1 chiều + Chặt nhị phân tìm vị trí tương thích gần nhất.

---
---

# CHƯƠNG 13: SELF-ASSESSMENT & PROGRESS TRACKING

> *"Những gì không thể đo lường thì không thể cải thiện."*

Hãy sử dụng bảng checklist Markdown dưới đây. Bạn có thể đánh dấu trực tiếp `[x]` vào file này sau mỗi buổi học để theo dõi sự tiến bộ thực tế của bản thân.

---

## 13.1. Checklist Năng lực Tư duy Cốt lõi (Thinking Capabilities)

- [ ] **Tư duy Vét cạn (Brute Force):** Khả năng tự viết code sinh không gian nghiệm $O(2^N)$ và $O(N!)$ trong vòng 5 phút để làm đối chứng.
- [ ] **Đọc hiểu Constraints:** Phản xạ nhìn giới hạn thời gian và $N$ để loại bỏ ngay lập tức các độ phức tạp bất khả thi.
- [ ] **Kỹ năng Chứng minh:** Có thể chứng minh tiêu chí sắp xếp của thuật toán Tham lam bằng Exchange Argument trước khi code.
- [ ] **Phát hiện tính đơn điệu:** Nhận biết khi nào hàm kiểm tra $P(X)$ thỏa mãn tính đơn điệu để kích hoạt Chặt nhị phân kết quả.
- [ ] **Tư duy Đảo ngược (Reverse Thinking):** Khả năng chuyển bài toán xóa đỉnh/cạnh thành thêm đỉnh/cạnh với DSU từ dưới lên.
- [ ] **Thiết kế Trạng thái DP:** Khả năng định nghĩa Tuple trạng thái tối thiểu mà không thừa thãi thông tin.
- [ ] **Tự động Stress Test:** Tự viết script sinh test ngẫu nhiên để bắt bug logic khi bị WA mà không cần nhìn test đề thi.

---

## 13.2. Checklist Cấu trúc dữ liệu & Thuật toán

### Cấu trúc dữ liệu
- [ ] Khắc phục triệt để nguy cơ Anti-Hash của `std::unordered_map` bằng Custom SplitMix64 Hash.
- [ ] Monotonic Stack: Tìm Nearest Smaller / Greater Element trong $O(N)$.
- [ ] Monotonic Queue: Sliding Window Maximum / Minimum trong $O(N)$.
- [ ] DSU với Path Compression & Union by Size ($O(\alpha(N))$).
- [ ] Fenwick Tree (Binary Indexed Tree): Point Add, Range Sum.
- [ ] Segment Tree: Point Update, Range Minimum/Sum Query.
- [ ] Segment Tree với Lazy Propagation: Range Add, Range Sum Query.
- [ ] Sparse Table: Static RMQ trong $O(1)$ truy vấn.
- [ ] Binary Lifting: Tổ tiên bậc $K$ và LCA trong $O(\log N)$.
- [ ] Ordered Set (`pb_ds`): `find_by_order` và `order_of_key`.

### Thuật toán Đồ thị
- [ ] BFS tìm đường đi ngắn nhất không trọng số & 0-1 BFS với `std::deque`.
- [ ] Dijkstra với `std::priority_queue` trên đồ thị trọng số không âm.
- [ ] Bellman-Ford & Phát hiện chu trình âm.
- [ ] Kruskal tìm Cây khung nhỏ nhất (MST) kết hợp DSU.
- [ ] Topological Sort với thuật toán Kahn.
- [ ] Tarjan tìm Thành phần liên thông mạnh (SCC) & Cầu/Khớp.
- [ ] Đường kính cây (2 lần BFS/DFS) & Trải phẳng cây (Euler Tour Technique).
- [ ] Luồng cực đại Dinic & Cặp ghép cực đại đồ thị hai phía.
- [ ] 2-SAT trên đồ thị suy diễn liên thông mạnh.

### Quy hoạch động (Dynamic Programming)
- [ ] Knapsack 0/1, Knapsack hoàn toàn (Unbounded), Tối ưu bộ nhớ 1D.
- [ ] Dãy con tăng dài nhất (LIS) trong $O(N \log N)$.
- [ ] Bitmask DP duyệt mọi tập con và duyệt Submask trong $O(3^N)$.
- [ ] Digit DP đếm số thỏa mãn điều kiện chữ số trong $[A, B]$.
- [ ] Tree DP tính toán từ lá lên gốc.
- [ ] Rerooting DP (2 lượt DFS đổi gốc cây trong $O(N)$).
- [ ] Tối ưu hóa DP bằng Mảng cộng dồn & Hàng đợi đơn điệu.

---

## 13.3. Sổ theo dõi Luyện tập Thực tế (Problem Solving Tracker)

| Ngày làm | Tên bài toán | Nền tảng | Rating | Thời gian nghĩ | Tự giải được? | Phải xem Editorial? | Cần giải lại? |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Ví dụ* | *Subarray Sums I* | *CSES* | *1100* | *15 phút* | *[x] Có* | *[ ] Không* | *[ ] Không* |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

---

## 13.4. Thang điểm Đánh giá Sẵn sàng cho ICPC 2027 (Readiness Metric)

- **Level 1 (Newbie $\to$ Pupil, Rating < 1400):** Cài đặt còn nhiều bug cú pháp, thường xuyên bị tràn số hoặc TLE do dùng cấu trúc dữ liệu sai.
  - *Giải pháp:* Tập trung làm toàn bộ các bài Fundamental ở Chương 10.
- **Level 2 (Specialist $\to$ Expert, Rating 1400 - 1800):** Đã làm chủ toàn bộ Cấu trúc dữ liệu cơ bản, giải tốt các bài Greedy, Binary Search và DP tiêu chuẩn. Đã sẵn sàng cho Kỳ thi Tin học tháng 12/2026!
- **Level 3 (Candidate Master $\to$ Master, Rating 1900 - 2300):** Nhận diện mô hình bài toán cực nhanh, nắm vững HLD, Centroid, DP Optimization, Luồng và 2-SAT. Đây là nòng cốt của các đội tuyển đạt giải cao tại ICPC National & Regional!
- **Level 4 (Grandmaster+, Rating 2400+):** Khả năng tự sáng tạo thuật toán mới cho bài toán chưa từng thấy, tư duy toán học và cấu trúc trực giác đạt độ thuần thục tối đa. Đủ năng lực tranh tài tại ICPC World Finals.

---

# LỜI KẾT TỪ HUẤN LUYỆN VIÊN

Con đường từ một sinh viên bắt đầu làm quen với Cấu trúc dữ liệu & Giải thuật đến khi bước lên bục vinh quang của đấu trường ICPC là một hành trình dài đầy thử thách, đòi hỏi sự kiên trì bền bỉ và tính kỷ luật thép. 

Sẽ có những ngày bạn ngồi 4 tiếng đồng hồ chỉ để tìm một lỗi sai dấu cộng/trừ trong bài toán Quy hoạch động. Sẽ có những kỳ thi bạn bị tụt rating hay nhận về hàng chục phán quyết Wrong Answer. Đó là điều **hoàn toàn bình thường**. Mọi Grandmaster hay World Finalist đều đã từng nộp bài sai hàng nghìn lần trước khi trở nên xuất sắc.

Hãy ghi nhớ nguyên tắc tối thượng: **Mỗi bài toán bạn không giải được sau khi xem Editorial và tự tay code lại thành công chính là khoảnh khắc tư duy của bạn vừa được nâng cấp lên một tầng cao mới.**

Chúc bạn giữ vững ngọn lửa đam mê, rèn luyện nghiêm túc theo lộ trình này và gặt hái thành công vang dội tại Kỳ thi Tin học tháng 12/2026 và ICPC 2027!
