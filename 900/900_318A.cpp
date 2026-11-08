#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n, k;
    cin >> n >> k;
    // 1 3 5 7 9 2 4 6 8
    if(n % 2){
        // n le
        if(k == n/2 + 1) cout << n << nl;
        else if(k < n/2 + 1){
            ll start = 1;
            ll res = start + (k - 1) * 2;
            cout << res<< nl;
        }
        else {
            ll start = 2;
            k = k - (n/2 + 1);
            ll res = start + (k - 1) * 2;
            cout << res << nl;
        }
    }
    else {
        // n chan
        // 1 3 5 7 2 4 6 8
        if(k <= n/2){
            ll start = 1;
            ll res = start + (k - 1) * 2;
            cout << res << nl;
        }
        else {
            ll start = 2;
            k = k - n/2;
            ll res = start + (k - 1) * 2;
            cout << res << nl;
        }
    }

    return 0;
}
