#include <iostream>
#include <set>
#include <algorithm>

#define DEGREE 2

using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    
    // n - node count, m - edge count
    // node range 1 ~ n -> so do not use 0 index element
    set<int> *graph = new set<int>[n+1];
    for (int i = 0; i < m; i++) {
        int start, end;
        cin >> start >> end;
        graph[start].insert(end);
        graph[end].insert(start);
    }

    // 1) find node with degree 2 - put them on set<int>
    set<int> node_set;
    for (int i = 1; i < n+1; i++) {
        if (graph[i].size() == DEGREE)
            node_set.insert(i);
    }

    int remove_cnt = 0;
    while (!node_set.empty()) {
        int curr = *node_set.begin();
        node_set.erase(curr);

        int first = *graph[curr].begin();
        int second = *graph[curr].rbegin();

        if (graph[first].find(second) == graph[first].end())
            continue;

        // removable curr ...
        ++remove_cnt;

        // remove curr node edges
        graph[curr].erase(first);
        graph[curr].erase(second);

        if (graph[first].size() == DEGREE)
            node_set.erase(first);
        if (graph[second].size() == DEGREE)
            node_set.erase(second);

        // remove neighbor node edges
        graph[first].erase(curr);
        graph[second].erase(curr);

        if (graph[first].size() == DEGREE)
            node_set.insert(first);
        if (graph[second].size() == DEGREE)
            node_set.insert(second);
    }

    delete[] graph;
    cout << n - remove_cnt << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    int test_case;
    cin >> test_case;

    for (int i = 0; i < test_case; i++) {
        cout << "Case #" << i+1 << "\n";
        solve();
    }
    return 0;
}
