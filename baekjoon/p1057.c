#include <stdio.h>

int main() {
    int n, k, h;
    int round = 0;
    scanf("%d %d %d", &n, &k, &h);

    k = k - 1;
    h = h - 1;

    while (k != h) {
        k = k >> 1;
        h = h >> 1;

        round++;
    }

    printf("%d\n", round);
    return 0;
}
