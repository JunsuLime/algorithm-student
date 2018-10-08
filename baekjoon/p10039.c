#include <stdio.h>

#define NUM_STUDENT 5

int main() {
    int i, tmp;
    int sum = 0;

    for (i = 0; i < NUM_STUDENT; i++) {
        scanf("%d", &tmp);
        if (tmp < 40) {
            sum += 40;
            continue;
        }
        sum += tmp;
    }

    printf("%d\n", sum / NUM_STUDENT);
    return 0;
}
