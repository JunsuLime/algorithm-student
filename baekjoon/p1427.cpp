#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <functional>

#define DIVIDER 10

using namespace std;

int main() {
    unsigned long long number;
    scanf("%llu", &number);

    vector<int> v;
    while (number) {
        v.push_back(number % DIVIDER);
        number /= DIVIDER;
    }

    sort(v.begin(), v.end(), greater<int>());

    vector<int>::iterator iter = v.begin();
    for (; iter != v.end(); ++iter) {
        printf("%d", *iter);
    }
    printf("\n");

    return 0;
}
