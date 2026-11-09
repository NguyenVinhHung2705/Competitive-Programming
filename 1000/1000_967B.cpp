#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, A, B; cin >> n >> A >> B;

    vector<int> a(n - 1);
    ll first_hole; cin >> first_hole;
    ll sum = first_hole;
    for(int i = 0;i<n-1;i++) {
        cin >> a[i];
        sum += a[i];
    }
    if(A == B) {
        cout << n - 1;
        return 0;
    }
    sort(a.begin(), a.end());
    int ans = 0;
    for(int i = n-2;i>=0;i--) {
        if(first_hole * A / sum >= B) {
            cout << ans;
            return 0;
        }
        else {
            ans++;
            sum -= a[i];
        }
    }
    cout << ans;


}
