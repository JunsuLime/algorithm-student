#include <stdio.h>
#include <string.h>

#define NUM_ALPHABET 26
#define CAPITAL_GAP 32
#define CAPITAL_START 65
#define SMALL_START 97

#define NORMALIZE_ALPHABET(c) c >= SMALL_START ? c - CAPITAL_GAP : c
#define ALPHABET_TO_IDX(c) c - CAPITAL_START
#define IDX_TO_ALPHABET(i) i + CAPITAL_START

#define IS_END(c) c == '\0' || c == '\n'

int main() {
    int num_alphabet[NUM_ALPHABET];
    int i;
    char c;

    char max_char;
    int num_max_char;
    int max_char_count;

    memset(num_alphabet, 0x00, sizeof(int) * NUM_ALPHABET);
    
    while (1) {
        c = getc(stdin);
        if (IS_END(c))
            break;

        c = NORMALIZE_ALPHABET(c);
        num_alphabet[ALPHABET_TO_IDX(c)]++;
    }

    max_char = '\0';
    num_max_char = 0;
    max_char_count = 0;

    for (i = 0; i < NUM_ALPHABET; i++) {
        if (num_alphabet[i] > num_max_char) {
            max_char = i;
            num_max_char = num_alphabet[i];
            max_char_count = 1;
        }
        else if (num_alphabet[i] == num_max_char) {
            max_char_count++;
        }
    }

    if (max_char_count != 1) {
        printf("?\n");
        return 0;
    }

    printf("%c\n", IDX_TO_ALPHABET(max_char));
    return 0;
}
