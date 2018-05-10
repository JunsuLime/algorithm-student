#include <iostream>

using namespace std;

int cached[1001][1001] = {0};

int main() {
    string a, b;
    cin >> a;
    cin >> b;
 
    for (int i = 1; i < a.size()+1; i++) {
        for (int j = 1; j < b.size()+1; j++) {
            if (a[i-1] == b[j-1]) { 
                cached[i][j] = cached[i-1][j-1] + 1;       
            }
            else {
                cached[i][j] = max(cached[i-1][j], cached[i][j-1]);
            }
        }
    }

    cout << cached[a.size()][b.size()] << endl;

    return 0;
}
