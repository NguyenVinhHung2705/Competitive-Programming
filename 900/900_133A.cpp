#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; cin >> s;
    for(int i = 0;i<s.length();i++) {
        if(s[i] == 'H' || s[i] == 'Q' || s[i] == '9') {
            cout << "YES";
            return 0;
        }
    }
    cout << "NO";

    return 0;
}
