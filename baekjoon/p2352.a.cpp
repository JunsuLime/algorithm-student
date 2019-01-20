#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    // index 0 is not used
    int *targets = new int[n+1];
    for (int i = 1; i <= n; i++) {
        scanf("%d", &targets[i]);
    }
    
    int *target_of_size = new int[n];
    int target;    
    target_of_size[1] = targets[1];
    int size = 1;

    for (int i = 2; i <= n; i++) {
        if (target_of_size[size] < targets[i]) {
            size++;
            target_of_size[size] = targets[i];
            continue;
        }
        int target_idx = lower_bound(target_of_size + 1, target_of_size + 1 + size, targets[i]) - target_of_size;
        target_of_size[target_idx] = targets[i];
    }

    printf("%d\n", size);
    return 0;
}
