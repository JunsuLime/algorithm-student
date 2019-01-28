#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFFER 2001
#define CHAR_TO_IDX(x) x - 'A'

int main() {

    int point[] = {3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1};

    char a[MAX_BUFFER];
    char b[MAX_BUFFER];

    memset(a, 0x00, sizeof(char) * MAX_BUFFER);
    memset(b, 0x00, sizeof(char) * MAX_BUFFER);

    scanf("%s", a);
    scanf("%s", b);

    int length = strlen(a);
    int scores[length * 2];

    for (int i = 0; i < length; i++) {
        scores[2 * i] = point[CHAR_TO_IDX(a[i])];
        scores[2 * i + 1] = point[CHAR_TO_IDX(b[i])];
    } 

    length = length * 2;
    while (length > 2) {
        for (int i = 0; i < length; i++) {
            scores[i] = (scores[i] + scores[i+1]) % 10;
        }

        length--;
    }

    printf("%d", scores[0]);
    printf("%d", scores[1]);

    printf("\n");
}
