#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double x, y;
    cin >> x >> y;

    int n = floor(log(y / x) / log(1.5)) + 1;

    cout << n;
}
