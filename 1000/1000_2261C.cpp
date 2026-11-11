
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    string p1 = "Moggity", p2 = "Larpity";
    while(t--) {
        int n; cin >> n;
        int odd = 0, even = 0;
        for(int i = 0;i<n;i++) {
            int x; cin >> x;
            if(x % 2 == 0) {
                even++;
            }
        }
        odd = n - even;
        if(odd == 1 && even == 1) {
            cout << p2 << nl;
        }
        else if(even == 0 && odd == 3) {
            cout << p2 << nl;
        }

        else {
            cout << p1 << nl;
        }
    }


}
