#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
void upper(char &c) {
    if(c >= 'a' && c <= 'z' ) {
        c -= 32;
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; cin >> s;
    upper(s[0]);
    cout << s;
}
