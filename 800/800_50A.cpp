#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int x, y; cin >> x >> y;
    int ans = 0;

    while(true) {
        if(y < 2) {
            if(x >= 2) {
                ans += x / 2;
                x = x % 2;
            }
        }
        else {
            ans += x * (y / 2);
            y = y % 2;
        }
        if(x == 0 || y == 0) {
            break;
        }
        if(x == 1 && y == 1) {
            break;
        }
    }
    cout << ans;
}
