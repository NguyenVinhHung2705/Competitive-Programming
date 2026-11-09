
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while(t--) {
        ll x, y; cin >> x >> y;
        cout << (y + 1 == x ? "NO" : "YES") << nl;
    }

}
