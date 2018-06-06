#include <stdio.h>
#include <algorithm>

using namespace std;

long long *num_list;
int n;

bool isExist(long long e) {
    // num_list is sorted list
    int left = 0;
    int right = n;
    int mid;

    while (left < right) {
        mid = (left + right) >> 1; // (l+r) / 2
        if (num_list[mid] == e)
            return true;
        else if (num_list[mid] > e) 
            right = mid;
        else
            left = mid + 1;
    }
    return false;
}

int main() {
    scanf("%d", &n);

    num_list = new long long[n];
    for (int i = 0; i < n; i++) {
        scanf("%lld", &num_list[i]);
    }
    sort(num_list, num_list+n);

    long long tmp;
    int m;
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%lld", &tmp);
        if (isExist(tmp))
            printf("1 ");
        else
            printf("0 ");
    }
    printf("\n");
    delete[] num_list;
    return 0;
}
