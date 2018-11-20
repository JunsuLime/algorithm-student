#include <stdio.h>

void solve() {
    int n, i;
    scanf("%d", &n);

    int scores[n];
    int sum = 0;
    for (i = 0; i < n; i++) {
        scanf("%d", &scores[i]);
        sum += scores[i];
    }

    double average = sum / n;
    int count = 0;
    for (i = 0; i < n; i++) {
        if (scores[i] > average)
            count++;
    }
    
    printf("%0.3lf\%%\n", (100 * (double) count) / n);
}

int main() {
    int test_case, i;
    scanf("%d", &test_case);

    for (i = 0; i < test_case; i++) {
        solve();
    }
    return 0;
}
