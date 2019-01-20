#include <stdio.h>

#define UNDEFINED -1
#define MAX(a, b) a > b ? a : b

// Complete search problem
// With dynamic programming


int *targets;
int n;

int get_max_conn(int idx, int recent_conn) {
    if (idx >= n)
        return 0;

    int conn1, conn2, max_conn;

    // try connect
    conn1 = 0;
    if (targets[idx] > recent_conn) {
        conn1 = get_max_conn(idx + 1, targets[idx]) + 1;
    }
    conn2 = get_max_conn(idx + 1, recent_conn);
    
    max_conn = MAX(conn1, conn2);
    return max_conn;
}

int main() {
    int i;
    scanf("%d", &n);

    targets = new int[n];

    for (i = 0; i < n; i++) {
        scanf("%d", &targets[i]);
    }

    printf("%d\n", get_max_conn(0, 0));

    delete[] targets;
    return 0;
}
