#include <stdio.h>
#include <stack>
#include <vector>

#define TRUE 1
#define PUSH '+'
#define POP '-'

#define INVALID_TOP -1

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
    int push_num = 1;
    int curr; // current referenced value of array
    int top;

    bool failure = false;
    for (int i = 0; i < n; i++) {
        curr = array[i];
        top = stack.empty() ? INVALID_TOP : stack.top();
        if (top != INVALID_TOP && stack.top() > curr) {
            failure = true;
            break;
        }
        
        while (top == INVALID_TOP || top < curr) {
            stack.push(push_num++);
            actions.push_back(PUSH);
            top = stack.top();
        }
        stack.pop();
        actions.push_back(POP);
    }
    delete[] array;

    // impossible case
    if (failure) {
        printf("NO\n");
        return 0;
    }

    vector<char>::iterator iter = actions.begin();
    for (iter; iter != actions.end(); ++iter) {
        printf("%c\n", *iter);
    }

    return 0;
}
