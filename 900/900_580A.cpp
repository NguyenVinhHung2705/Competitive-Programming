#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;cin >> n;
    int pre;cin >> pre;int dem = 1, mxDem = 1;
    for(int i = 1;i<n;i++) {
        int x; cin >> x;
        if(x >= pre) {
            dem ++;
            mxDem = max(mxDem, dem);
        }
        else {
            dem = 1;
        }
        pre = x;
    }
    cout << mxDem;
}
