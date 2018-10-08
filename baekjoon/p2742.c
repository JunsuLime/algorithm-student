#include <stdio.h>

int main() {
    unsigned int i = 0;
    unsigned int n;
    scanf("%d", &n);

    for (i = n; i > 0; i--) {
        printf("%d\n", i);
    }

    return 0;
}
