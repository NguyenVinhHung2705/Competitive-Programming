#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r, g,b; cin >> r >> g >> b;
    int Dr = (r+1)/2, Dg = (g+1)/2, Db = (b+1)/2;
    cout << 30 + max({3 * (Dr - 1), 1 + 3 * (Dg - 1), 2 + 3 * (Db -1)});
}
