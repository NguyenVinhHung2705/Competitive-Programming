#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; cin >> s;
    int n = s.length(), dem = 1;
    for(int i = 1;i<n;i++) {
        if(s[i] == s[i-1]) {
            dem++;
        }
        else {
            dem = 1;
        }
        if(dem == 7) {
            cout << "YES";
            return 0;
        }
    }
    cout << "NO";


}
