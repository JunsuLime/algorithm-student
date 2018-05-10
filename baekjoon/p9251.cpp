#include <iostream>
#include <algorithm>

using namespace std;

string a, b;
int cached[1001][1001] = {0};

int lcs(int cur_a, int cur_b) {
    if (cached[cur_a][cur_b] != 0) {
        return cached[cur_a][cur_b];
    }
    if (cur_a == a.size()) {
        return 0;
    }
    if (cur_b == b.size()) {
        return 0;
    }   

    int max_length = 0;
    for (int i = cur_a+1; i < a.size(); i++) {
        for (int j = cur_b+1; j < b.size(); j++) {
            if (a[i] == b[j]) {
                max_length = max(max_length, lcs(i, j)+1);
                break;
            }
        }
    }

    cached[cur_a][cur_b] = max_length;
    return max_length;
}

int main() {

    cin >> a;
    cin >> b;

    int max_length = 0;
    for (int i = 0; i < a.size(); i++) {
        for (int j = 0; j < b.size(); j++) {
            if (a[i] == b[j]) {
                max_length = max(max_length, lcs(i, j)+1);
                break;
            }
        }
    }
    
    cout << max_length << endl;
    
    return 0;
}
