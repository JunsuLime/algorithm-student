#include <stdio.h>
#include <queue>
#include <vector>

#define INFINITY -1
#define UNDEFINED -2

using namespace std;

struct Edge {
    int weight;
    int destination;

    Edge(int weight, int destination) {
        this->weight = weight;
        this->destination = destination;
    }

    bool operator>(const Edge& e) const {
        if (e.weight == INFINITY)
            return false;

        return weight > e.weight;
    }
};

void print_distance(int d) {
    if (d == INFINITY) {
        printf("INF\n");
        return;
    }

    printf("%d\n", d);
}

void print_edge(Edge *e) {
    printf("destination = %d, weight = %d\n", e->destination, e->weight);
}

int main() {
    int v, e;
    scanf("%d %d", &v, &e);
    int start;
    scanf("%d", &start);
    
    // 0 index is not used
    vector<Edge> graph[v+1];
    int start_point, end_point, weight;
    for (int i = 0; i < e; i++) {
        // u, v, w
        scanf("%d %d %d", &start_point, &end_point, &weight);
        graph[start_point].push_back(Edge(weight, end_point));
    }

    int distances[v+1];
    int prev_distances[v+1];

    distances[start] = 0;
    
    /////// Dijkstra
    priority_queue<Edge, vector<Edge>, greater<Edge> > queue;

    for (int i = 1; i <= v; i++) {
        if (i != start)
            distances[i] = INFINITY;
        
        prev_distances[i] = UNDEFINED;
    }

    queue.push(Edge(distances[start], start));
    
    while (!queue.empty()) {
        Edge e = queue.top();
        queue.pop();

        vector<Edge>::iterator iter = graph[e.destination].begin();
        for (; iter != graph[e.destination].end(); ++iter) {
            int weight_sum = distances[e.destination] + (*iter).weight;
            if (distances[(*iter).destination] == INFINITY ||
                    weight_sum < distances[(*iter).destination]) {
                distances[(*iter).destination] = weight_sum;
                prev_distances[(*iter).destination] = e.destination;

                queue.push(Edge(weight_sum, (*iter).destination));
            }
        }
    }

    /////// Dijkstra end
    
    for (int i = 1; i <= v; i++) {
        print_distance(distances[i]);
    }

}
