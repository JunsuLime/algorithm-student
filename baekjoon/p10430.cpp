#include <stdio.h>

int main() {
    unsigned int a, b, c;
    unsigned int answer1, answer2;
    scanf("%d %d %d", &a, &b, &c);

    answer1 = (a + b) % c;
    answer2 = (a * b) % c;
    printf("%d\n%d\n%d\n%d\n", answer1, answer1, answer2, answer2);
}
