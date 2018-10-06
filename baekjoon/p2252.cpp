#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

struct Node {
    int id;
    vector<int> taller;
    int degree = 0;
};

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    
    Node nodes[n+1];
    int a, b;
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &a, &b);
        nodes[a].taller.push_back(b);
        nodes[b].degree++;
    }

    queue<Node*> q;
    for (int i = 1; i <= n; i++) {
        nodes[i].id = i;
        if (nodes[i].degree == 0)
            q.push(&nodes[i]);
    }


    while (!q.empty()) {
        Node *node = q.front();
        q.pop();
        printf("%d ", node->id);

        vector<int>::iterator iter = node->taller.begin();
        for (; iter != node->taller.end(); ++iter) {
            nodes[*iter].degree--;
            if (nodes[*iter].degree == 0) 
                q.push(&nodes[*iter]);
        }
    }
    printf("\n");

    return 0;
}
