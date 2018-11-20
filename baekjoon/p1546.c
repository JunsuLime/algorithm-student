#include <stdio.h>

#define INVALID -1

int main() {
    int n, i;
    scanf("%d", &n);

    int max = INVALID;
    int scores[n];
    double sum = 0;
    for (i = 0; i < n; i++) {
        scanf("%d", &scores[i]);
        sum += scores[i];
        if (max == INVALID || max < scores[i]) {
            max = scores[i];
        }
    }

    double average = sum / n;
    double modified = (average * 100) / max;

    printf("%0.3lf\n", modified);
    return 0;
}
