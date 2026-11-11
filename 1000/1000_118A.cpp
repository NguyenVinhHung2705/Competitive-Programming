#include <bits/stdc++.h>

using namespace std;



#define ll long long
#define nl '\n'
void lower(char& c) {
    if(c >= 'A' && c <= 'Z') {
        c += 32;
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; cin >> s;
    string ans = "";
    for(auto& c : s) {
        lower(c);
        if(c != 'a' && c != 'u' && c != 'o' && c != 'e' && c != 'i' && c != 'y') {
            ans += ".";
            ans += c;
        }
    }
    cout << ans;

}
