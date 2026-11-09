#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll x; cin >> x;
    if(x == 0) {
        cout << 0;
        return 0;
    }
    if(x % 2 == 1) {
        cout << (x + 1) / 2;
    }
    else {
        cout << (x + 1);
    }

}
