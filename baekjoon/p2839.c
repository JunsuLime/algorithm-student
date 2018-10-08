#include <stdio.h>

#define HEAVY 5
#define LIGHT 3

int main() {
    int n, remain;
    int total_burden;
    int heavy_burden;

    scanf("%d", &n);

    heavy_burden = n / HEAVY;
    while (heavy_burden >= 0) {
        remain = n - heavy_burden * HEAVY;
        if (remain % LIGHT == 0) {
            printf("%d\n", heavy_burden + (remain / LIGHT));
            return 0;
        }
        
        heavy_burden--;
    }

    printf("%d\n", -1);
    return 0;
}
