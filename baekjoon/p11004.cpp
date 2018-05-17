#include <iostream>
#include <algorithm>

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);

    int n, k;
    cin >> n >> k;

    int *array = (int*) malloc(sizeof(int)*n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }

    sort(array, array+n);
    cout << array[k-1] << endl;
    free(array);

    return 0;
}
