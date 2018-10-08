#include <stdio.h>
#include <math.h>

int square(int n) {
    return n * n;
}

int max(int n1, int n2) {
    return n1 > n2 ? n1 : n2;
}

int min(int n1, int n2) {
    return n1 < n2 ? n1 : n2;
}

void solve() {
    int x1, y1, r1, x2, y2, r2;
    int max_radius, min_radius;
    double distance_square;

    scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

    if (x1 == x2 && y1 == y2 && r1 == r2) {
        printf("-1\n");
        return;
    }

    max_radius = max(r1, r2);
    min_radius = min(r1, r2);
    distance_square = square(x1 - x2) + square(y1 - y2);

    // no intersection
    if (distance_square < square(max_radius - min_radius) || square(r1 + r2) < distance_square) {
        printf("0\n");
        return;
    }

    // only one intersection
    if (square(r1 + r2) == distance_square 
            || square(max_radius - min_radius) == distance_square) {
        printf("1\n");
        return;
    }
    printf("2\n");
}

int main() {
    int i;
    int test_case;

    scanf("%d", &test_case);

    for (i = 0; i < test_case; i++) {
        solve();
    }

}
