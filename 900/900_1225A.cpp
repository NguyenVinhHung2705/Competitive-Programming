
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define nl '\n'
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int a, b; cin >> a >> b;
    if(a == 9 && b == 1){
        cout << 9 << " " << 10;
    }
    else if( abs(a-b) > 1 || a > b) {
        cout << -1;
    }
    else if(a==b){
        cout << a * 10  << " " << a * 10 + 1;
    }
    else{
        cout << a* 10 + 9 << " " << b * 10;
    }
}
