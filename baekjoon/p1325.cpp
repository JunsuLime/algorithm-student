#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

void reset_bool_list(bool *list, int n) {
    for (int i = 0; i < n; i++) {
        list[i] = false;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;

    // index 0 is not used
    vector<int> *graph = new vector<int>[n+1];
    int start, end;
    for (int i = 0; i < m; i++) {
        cin >> end >> start;
        graph[start].push_back(end);
    }

    int max_cluster_cnt = 0;
    vector<int> max_cluster_list;
    bool *visited = new bool[n+1];
    
    stack<int> node_stack;
    // index is started from 1, end with n (0 is not used)
    for (int i = 1; i < n+1; i++) {
        
        reset_bool_list(visited, n+1);
        int cluster_cnt = 0;

        node_stack.push(i);
        visited[i] = true;
        cluster_cnt++;

        while(!node_stack.empty()) {
            int curr = node_stack.top();
            node_stack.pop();

            vector<int>::iterator node_iter = graph[curr].begin();
            for (; node_iter != graph[curr].end(); ++node_iter) {
                int next = *node_iter;
                if (visited[next])
                    continue;

                node_stack.push(next);
                visited[next] = true;
                cluster_cnt++;
            }
        }
        if (cluster_cnt > max_cluster_cnt) {
            max_cluster_cnt = cluster_cnt;
            max_cluster_list.clear();
            max_cluster_list.push_back(i);
        }
        else if (cluster_cnt == max_cluster_cnt) {
            max_cluster_list.push_back(i);
        }
    }

    sort(max_cluster_list.begin(), max_cluster_list.end());
    vector<int>::iterator iter = max_cluster_list.begin();
    for (; iter != max_cluster_list.end(); ++iter) {
        cout << *iter << " ";
    }
    cout << endl;
}

