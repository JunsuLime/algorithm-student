#include <stdio.h>
#include <queue>
#include <vector>

#define INFINITY -1

using namespace std;

struct Edge {
    int dest;
    int fee;

    Edge(int dest, int fee) {
        this->dest = dest;
        this->fee = fee;
    }

    bool operator>(const Edge& e) const {
        if (e.fee == INFINITY)
            return false;

        return fee > e.fee;
    }
};

int main() {

    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);

    // index 0 is not used. 1 ~ n
    vector<Edge> graph[n+1];

    int start, end, fee;
    for (int i = 0; i < m; i++) {
        // start, end, weight
        scanf("%d %d %d", &start, &end, &fee);
        graph[start].push_back(Edge(end, fee));
    }

    scanf("%d %d", &start, &end);

    // 0 is not used;
    int paths[n+1];
    // initialize all paths to INFINITY
    for (int i = 1; i <= n; i++) {
        paths[i] = INFINITY;
    }
    paths[start] = 0;

    priority_queue<Edge, vector<Edge>, greater<Edge> > queue;
    queue.push(Edge(start, paths[start]));

    while (!queue.empty()) {
        Edge path = queue.top();
        queue.pop();

        vector<Edge>::iterator connected = graph[path.dest].begin();

        for (; connected != graph[path.dest].end(); ++connected) {
            int dest = (*connected).dest;
            int sum_fee = path.fee + (*connected).fee;
            int compare_fee = paths[dest];
            if (compare_fee == INFINITY || sum_fee < compare_fee) {
                paths[dest] = sum_fee;
                queue.push(Edge(dest, sum_fee));
            }
        }
    }

    printf("%d\n", paths[end]);
}
