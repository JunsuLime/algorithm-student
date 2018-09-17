#include <stdio.h>
#include <stack>
#include <vector>

#define TRUE 1
#define PUSH '+'
#define POP '-'

using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    int *array = new int[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    stack<int> stack;
    vector<char> actions;
    int top;
    int curr = 0; // current reference on array

    // push 1~n to stack
    for (int i = 1; i <= n; i++) {
        stack.push(i);
        actions.push_back(PUSH);
        while (!stack.empty()) {
            top = stack.top();
            if (top != array[curr])
                break;

            curr++;
            stack.pop();
            actions.push_back(POP);
        }
    }

    delete[] array;

    // impossible case
    if (curr != n) {
        printf("NO\n");
        return 0;
    }

    vector<char>::iterator iter = actions.begin();
    for (iter; iter != actions.end(); ++iter) {
        printf("%c\n", *iter);
    }

    return 0;
}
