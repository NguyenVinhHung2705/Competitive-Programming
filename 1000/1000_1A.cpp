#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n, m, a; cin >> n >> m >> a;
    ll x, y;
    x = n / a;
    y = m / a;
    if(n % a != 0) {
        x++;
    }
    if(m % a != 0) {
        y++;
    }
    cout << x * y;


}
