#include <iostream>
#include <stack>

#define OFFSET 65
#define NONE -1
#define ROOT 0

using namespace std;

struct Node {
    int left = NONE;
    int right = NONE;
};

int main() {
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;

    Node *node_list = new Node[n];
    char ch;
    for (int i = 0; i < n; i++) {
        int root, left, right;
        cin >> ch;
        root = ch - OFFSET;
        
        cin >> ch;
        if (ch == '.')
            left = NONE;
        else
            left = ch - OFFSET;
        
        cin >> ch;
        if (ch == '.')
            right = NONE;
        else
            right = ch - OFFSET;
        
        node_list[root].left = left;
        node_list[root].right = right;
    }

    stack<int> traverse;
    stack<int> stack;
    int curr;

    // 1) pre-order traversal
    stack.push(ROOT);

    while(!stack.empty()) {
        curr = stack.top();
        cout << (char) (curr + OFFSET);
        stack.pop();
        
        int left = node_list[curr].left;
        int right = node_list[curr].right;

        if (right != NONE)
            stack.push(right);
        if (left != NONE)
            stack.push(left);
    }
    cout << endl;

    // 2) in-order traversal
    curr = ROOT;
    while (curr != NONE) {
        stack.push(curr);
        curr = node_list[curr].left;
    }
    
    while (!stack.empty()) {
        curr = stack.top();
        stack.pop();
        cout << (char) (curr + OFFSET);

        curr = node_list[curr].right;
        while (curr != NONE) {
            stack.push(curr);
            curr = node_list[curr].left;
        }
    }
    cout << endl;

    // 3) post-order traversal
    curr = ROOT;

    stack.push(ROOT);
    while (!stack.empty()) {
        curr = stack.top();
        traverse.push(curr);
        stack.pop();
        
        int left, right;
        left = node_list[curr].left;
        right = node_list[curr].right;
        if (left != NONE) 
            stack.push(left);
        if (right != NONE)
            stack.push(right);
    }

    while (!traverse.empty()) {
        cout << (char) (traverse.top() + OFFSET);
        traverse.pop();
    }
    cout << endl;

    delete[] node_list;
    return 0;
}
