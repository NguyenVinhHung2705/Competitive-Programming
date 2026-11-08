#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int  x, y;
    bool flag = false;
    for(int i = 0;i<5;i++) {
        if(flag) break;
        for(int j = 0;j<5;j++) {
            int tmp; cin >> tmp;
            if(tmp == 1) {
                x = i;
                y = j;
                flag = true;
                break;
            }
        }
    }
    cout << (abs(x - 2) + abs(y - 2));

}
