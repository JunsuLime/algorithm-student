#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int n, tmp;
    cin >> n;

    vector<int> v;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        v.push_back(tmp);    
    }

    sort(v.begin(), v.end(), greater<int>());

    int lope_count = 1;
    long max_weight = 0;

    vector<int>::iterator iter = v.begin();
    for (; iter != v.end(); iter++) {
        int weight = *iter * lope_count;
        if (max_weight < weight) {
            max_weight = weight;
        }
        lope_count++;
    }
    cout << max_weight << endl;
}
