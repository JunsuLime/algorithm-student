#include <stdio.h>

int main() {
    int score;
    scanf("%d", &score);

    if (score >= 90) {
        printf("A\n");
        return 0;
    }
    else if (score >= 80) {
        printf("B\n");
        return 0;
    }
    else if (score >= 70) {
        printf("C\n");
        return 0;
    }
    else if (score >= 60) {
        printf("D\n");
        return 0;
    }
    
    printf("F\n");
    return 0;
}
