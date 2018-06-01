#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    
    int n, k, tmp, curr;
    cin >> n >> k;

    vector<int> v;
    curr = -1;
    // because 1 is exist -> all case can be made
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        if (tmp < k) {
            v.push_back(tmp);
            curr++;
        }
    }

    // curr is last index of vector container
    int count = 0;
    for (; curr >= 0; curr--) {
       if (k == 0)
           break;
       if (v[curr] > k)
           continue;

       int div =  k / v[curr];
       count += div;
       k -= v[curr] * div;
    }

    cout << count << endl;

    return 0;
}
