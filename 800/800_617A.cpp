
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int x; cin >> x;
    int ans = x / 5;
    cout << (x % 5 != 0 ? ans + 1 : ans);
}
