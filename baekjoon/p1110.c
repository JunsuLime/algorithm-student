#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int first, second, tmp;
    first = n / 10;
    second = n % 10;

    int cycle = 0;
    while (1) {
        tmp = first;
        first = second;
        second = (tmp + second) % 10;
        cycle++;

        if (first * 10 + second == n)
            break;
    }

    printf("%d\n", cycle);
    return 0;
}
