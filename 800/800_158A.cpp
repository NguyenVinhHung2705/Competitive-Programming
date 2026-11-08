
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k; cin >> n >> k;
    int x = 0;
    vector<int> a(n);
    for(int i = 0;i<n;i++) {
        cin >> a[i];
    }
    int tmp = a[k-1];
    sort(a.begin(), a.end());
    for(int i = n-1;i >= 0;i--) {
        if(a[i] != 0) {
            if(a[i] >= tmp) {
                x++;
            }
            else {
               break;
            }
        }

    }
    cout << x;


}
