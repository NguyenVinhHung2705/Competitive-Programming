#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
void to_lower(char &x) {
    if(x >= 'A' && x <= 'Z') {
        x += 32;
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1, s2; cin >> s1; cin >> s2;
    int n = s1.length();
    for(int i = 0;i<n;i++) {
        to_lower(s1[i]);
        to_lower(s2[i]);
        if(s1[i] - 'a' > s2[i] - 'a') {
            cout << 1;
            return 0;
        }
        else if(s1[i] - 'a' < s2[i] - 'a') {
            cout << -1;
            return 0;
        }
    }
    cout << 0;
}
