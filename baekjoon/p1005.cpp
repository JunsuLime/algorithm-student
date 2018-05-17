#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Node {
    int b_time = 0;
    int degree = 0;
    vector<int> next;

    bool operator>(Node n) const {
        return b_time > n.b_time;
    }
};

void work() {
    int b_num, r_num;
    cin >> b_num >> r_num;

    vector<Node> nodes;

    for (int i = 0; i < b_num; i++) {
        int b_time;
        cin >> b_time;
        Node node;
        node.b_time = b_time;
        nodes.push_back(node);
    }

    nodes.resize(b_num);

    for (int i = 0; i < r_num; i++) {
        int start, end;
        cin >> start >> end;

        start--;
        end--;

        nodes[start].next.push_back(end);
        nodes[end].degree++;
    }

    int final_b;
    cin >> final_b;
    final_b--;

    priority_queue<Node, vector<Node>, greater<Node>> queue;
    int finish_time = 0;

    for (int i = 0; i < b_num; i++) {
        if (nodes[i].degree == 0) {
            queue.push(nodes[i]);
        }
    }

    while (!queue.empty()) {
        Node cur = queue.top();
        queue.pop();

        bool finished = false;
        vector<int>::iterator iter = cur.next.begin();
        for (; iter != cur.next.end(); iter++) {
            Node *next_node = &nodes[*iter];
            next_node->degree--;
            if (next_node->degree == 0) {
                next_node->b_time += cur.b_time;
                if (*iter == final_b) {
                    finish_time = next_node->b_time;
                    finished = true;
                    break;
                }
                queue.push(*next_node);
            }
        }
        if (finished) {
            break;
        }
    }

    cout << finish_time << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    int test_case;

    cin >> test_case;
    for (int i = 0; i < test_case; i++) {
        work();
    }
}
