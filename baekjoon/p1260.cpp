#include <stdio.h>
#include <set>
#include <stack>
#include <queue>

using namespace std;

void __dfs_search(set<int> *graph, int current, bool *visited) {
    if (visited[current])
        return;

    visited[current] = true;
    printf("%d ", current);

    set<int>::iterator neighbor_iter = graph[current].begin();
    for (; neighbor_iter != graph[current].end(); ++neighbor_iter) {
        __dfs_search(graph, *neighbor_iter, visited);
    }
}

void dfs_search(set<int> *graph, int start, int n) {
    // initialize all false
    bool visited[n+1] = {};

    __dfs_search(graph, start, visited);

    printf("\n");
}

void bfs_search(set<int> *graph, int start, int n) {
    bool visited[n+1] = {};
    queue<int> queue;
    queue.push(start);
    visited[start] = true;

    int current;
    set<int>::iterator neighbor_iter;
    while (!queue.empty()) {
        current = queue.front();
        printf("%d ", current);
        queue.pop();

        neighbor_iter = graph[current].begin();
        for (; neighbor_iter != graph[current].end(); ++neighbor_iter) {
            if (visited[*neighbor_iter])
                continue;
            queue.push(*neighbor_iter);
            visited[*neighbor_iter] = true;
        }
    }

    printf("\n");
}

int main() {

    int n, m, v;
    scanf("%d %d %d", &n, &m, &v);

    // 0 index is not used
    // set is sorted data structure (default ascending)
    set<int> *graph = new set<int>[n+1];
    int node1, node2;

    for (int i = 0; i < m; i++) {
        scanf("%d %d", &node1, &node2);
        // bidirectional graph
        graph[node1].insert(node2);
        graph[node2].insert(node1);
    }

    dfs_search(graph, v, n);
    bfs_search(graph, v, n);

    return 0;
}
