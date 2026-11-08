#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while(t--) {
        ll n, k; cin >> n >> k;
        ll a, b, c, d;
        a = (double)n / (double)((k + 1) * (k * k + 1));
        b = a * k;
        c = b * k;
        d = c * k;
        cout << a << " " << b << " " << c << " " << d << nl;
    }
}
