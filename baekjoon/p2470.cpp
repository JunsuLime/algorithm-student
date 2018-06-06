#include <iostream>
#include <vector>
#include <algorithm>

#define UNDEFINED -1

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    
    vector<long long> acid_list;
    vector<long long> base_list;

    long long tmp;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        if (tmp >= 0)
            acid_list.push_back(tmp);
        else
            base_list.push_back(tmp);
    }
    
    sort(acid_list.begin(), acid_list.end());
    sort(base_list.begin(), base_list.end(), greater<long long>());

    if (acid_list.size() == 0) {
        cout << base_list[1] << " ";
        cout << base_list[0] << endl;
    }
    else if (base_list.size() == 0) {
        cout << acid_list[0] << " ";
        cout << acid_list[1] << endl;
    }
    else {
        long long min_acid = acid_list[0];
        long long min_base = base_list[0];
        long long min_diff = min_acid + min_base;
        if (min_diff == 0) {
            cout << min_base << " ";
            cout << min_acid << endl; 
            return 0;
        }

        int acid_idx = 0;
        int base_idx = 0;
        while (acid_idx != acid_list.size() && base_idx != base_list.size()) {
            long long diff = acid_list[acid_idx] + base_list[base_idx];
            if (diff == 0) {
                min_acid = acid_list[acid_idx];
                min_base = base_list[base_idx];
                break;
            }
            if (abs(min_diff) > abs(diff)) {
                min_acid = acid_list[acid_idx];
                min_base = base_list[base_idx];
                min_diff = diff;
            }

            if (acid_idx == acid_list.size()-1) 
                ++base_idx;   
            else if (base_idx == base_list.size()-1) 
                ++acid_idx;
            else if (diff > 0)
                ++base_idx;
            else 
                ++acid_idx;
        } 
        cout << min_base << " ";
        cout << min_acid << endl;
    }
    return 0;
}
