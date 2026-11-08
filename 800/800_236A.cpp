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
    string s; cin >> s;
    int freq[26] = {0}, n = s.length(), distinct = 0;
    for(int i = 0;i<n;i++) {
        int index = s[i] - 'a';
        if(freq[index] == 0) {
            distinct++;
            freq[index] = 1;
        }
    }
    cout << (distinct % 2 == 0 ? "CHAT WITH HER!" : "IGNORE HIM!");
}
