#include <stdio.h>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    priority_queue<int, vector<int>, greater<int> > queue;
    for (int i = 0; i < n; i++) {
        int number;
        scanf("%d", &number);
        queue.push(number);
    }

    while (!queue.empty()) {
        printf("%d\n", queue.top());
        queue.pop();
    }

    return 0;
}
