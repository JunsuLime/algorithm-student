#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define EMPTY   0
#define HOUSE   1
#define VISITED 2

#define MAX_ROW 25
#define DIRECTION_CNT   4

using namespace std;

int direction[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int graph[MAX_ROW][MAX_ROW];


int getClusterItemCount(int n, int x, int y) {
    
    int cluster_item_cnt = 0;
    stack<pair<int, int> > coord_stack;
    
    graph[x][y] = VISITED;
    coord_stack.push(pair<int, int>(x, y));

    // DFS search with stack
    while (!coord_stack.empty()) {
        pair<int, int> curr = coord_stack.top();
        coord_stack.pop();
        cluster_item_cnt++;

        for (int i = 0; i < DIRECTION_CNT; i++) {
            int nx = curr.first + direction[i][0];
            int ny = curr.second + direction[i][1];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                continue;
            if (graph[nx][ny] != HOUSE)
                continue;
            
            graph[nx][ny] = VISITED;
            coord_stack.push(pair<int, int>(nx, ny));
        }
    }
    return cluster_item_cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;

    string tmp;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        for (int j = 0; j < n; j++) {
            if (tmp[j] == '1')
                graph[i][j] = HOUSE;
            else
                graph[i][j] = EMPTY;
        }
    }

    int cluster_count = 0;
    vector<int> cnt_list;
    for (int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if (graph[i][j] != HOUSE) 
                continue;
            cnt_list.push_back(getClusterItemCount(n, i, j));
            cluster_count++;
        }
    }

    cout << cluster_count << endl;

    sort(cnt_list.begin(), cnt_list.end());
    vector<int>::iterator cnt_iter = cnt_list.begin();
    for (; cnt_iter != cnt_list.end(); cnt_iter++) {
        cout << *cnt_iter << endl;
    }   

    return 0;
}
