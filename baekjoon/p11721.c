#include <stdio.h>

#define MAX_LEN 10
#define IS_END(c) c == '\n' || c == '\0'

int main() {
    char c;
    int count = 0;

    while (1) {
        scanf("%1c", &c);
        if (IS_END(c))
            break;
        count++;

        printf("%c", c);
        if (count == MAX_LEN) {
            count = 0;
            printf("\n");
        }
    }

    return 0;
}
