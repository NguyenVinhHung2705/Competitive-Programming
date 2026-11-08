
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<int> a(n);int sum = 0;
    for(int i = 0;i<n;i++) {
        cin >> a[i];
        sum += a[i];
    }
    sort(a.begin(), a.end());
    int x = a[n-1], dem = 1;
    sum -= x;
    for(int i = n-2;i>=0;i--) {
        if(x > sum) {
            cout << dem;
            return 0;
        }
        sum -= a[i];
        x += a[i];
        dem++;
    }
    cout << n;
}
