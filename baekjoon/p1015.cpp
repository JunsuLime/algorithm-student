#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Item {
    int idx;
    int val;
    Item(int idx, int val) {
        this->idx = idx;
        this->val = val;
    }

    bool operator< (Item item) const {
        if (val < item.val)
            return true;
        else if (val == item.val)
            return idx < item.idx;
        else
            return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
   
    vector<Item> item_list;
    int tmp;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        item_list.push_back(Item(i, tmp));
    }

    sort(item_list.begin(), item_list.end());
    int *num_list = new int[n];
    for (int i = 0; i < n; i++) {
        num_list[item_list[i].idx] = i;
    }
    
    for (int i = 0; i < n; i++) {
        cout << num_list[i] << " ";
    }
    cout << endl;

    delete[] num_list;
    return 0;
}
