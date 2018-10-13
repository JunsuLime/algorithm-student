#include <stdio.h>

#define START_SMALL_A 97

int alphabet_arr[26];
char input_string[100];

int main() {
    char c;
    int i;
    int position = 0;

    scanf("%s", input_string);

    for (i = 0; i < 26; i++) {
        alphabet_arr[i] = -1;
    }

    while (1) {
        c = input_string[position];
        if (c == '\0')
            break;
        if (alphabet_arr[c - START_SMALL_A] == -1)
            alphabet_arr[c - START_SMALL_A] = position;
        position++;
    }
    for (i = 0; i < 26; i++) {
        printf("%d ", alphabet_arr[i]);
    }
    printf("\n");

    return 0;
}
