#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<int> a(n);
    for(int i = 0;i<n;i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    for(const auto& x : a) {
        cout << x <<  " ";
    }

    return 0;
}
