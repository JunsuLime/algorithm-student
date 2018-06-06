#include <iostream>

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    string s;
    cin >> s;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] >= 'A' && s[i] <= 'Z')
            cout << s[i];
    }
    cout << endl;
}
