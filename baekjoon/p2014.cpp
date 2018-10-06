#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>

#define INVALID_NUM 0
#define MAX_ANSWER 1 << 31

using namespace std;

int main() {

    int k, n;
    scanf("%d %d", &k, &n);

    unsigned long long int array[k];
    priority_queue<
        unsigned long long int, 
        vector<unsigned long long int>,
        greater<unsigned long long int> 
    > queue;

    for (int i = 0; i < k; i++) {
        scanf("%llu", &array[i]);
        queue.push(array[i]);
    }

    int count = 0;
    unsigned long long int prev = INVALID_NUM;
    unsigned long long int curr = INVALID_NUM;
    while (!queue.empty()) {
        curr = queue.top();
        queue.pop();

        if (prev == curr) 
            continue;
        if (++count == n)
            break;

        for (int i = 0; i < k; i++) {
            queue.push(array[i] * curr);
            if (curr % array[i] == 0)
                break;
        }

        prev = curr;
    }

    printf("%llu\n", curr);
    return 0;
}
