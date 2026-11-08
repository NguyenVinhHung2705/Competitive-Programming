#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
void swap_char(char &source, char target) {
    source = target;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int a[4] = {0};
    string s; cin >> s;
    for(const auto& c : s) {
        if (c == '1') {
            a[1]++;
        }
        else if(c == '2') {
            a[2]++;
        }
        else if(c == '3') {
            a[3]++;
        }
    }
    int i = 0;
    while(a[1] > 0) {
        swap_char(s[i], '1');
        i += 2;
        a[1]--;
    }
    while(a[2] > 0) {
        swap_char(s[i], '2');
        i += 2;
        a[2]--;
    }
    while(a[3] > 0) {
        swap_char(s[i], '3');
        i += 2;
        a[3]--;
    }
    cout << s;
}
