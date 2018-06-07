#include <iostream>
#include <algorithm>
#include <string.h>

#define UNDEFINED -1

using namespace std;

long long cache[2000][2000];

int *x_list;
int *y_list;
int n;

long long getDistance(int x, int y) {
    return (x-y) * (x-y);
}
long long getDistanceSum(int x_idx, int y_idx) {
    if (cache[x_idx][y_idx] != UNDEFINED) {
        return cache[x_idx][y_idx];
    }

    long long distance = 0;
    if (x_idx == n-1) {
        for (int i = y_idx; i < n; i++) {
            distance += getDistance(x_list[x_idx], y_list[i]);
        }
        return distance;
    }
    else if (y_idx == n-1) {
        for (int i = x_idx; i < n; i++) {
            distance += getDistance(x_list[i], y_list[y_idx]);
        }
        return distance;
    }

    distance = getDistance(x_list[x_idx], y_list[y_idx]);
    
    long long min_val;
    min_val = min(getDistanceSum(x_idx+1, y_idx), getDistanceSum(x_idx, y_idx+1));
    min_val = min(getDistanceSum(x_idx+1, y_idx+1), min_val);

    cache[x_idx][y_idx] = distance + min_val;
    return distance + min_val;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n;

    memset(cache, UNDEFINED, sizeof(long)*2000*2000);
    x_list = new int[n];
    y_list = new int[n];

    for (int i = 0; i < n; i++) {
        cin >> x_list[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> y_list[i];
    }

    long long distance = getDistanceSum(0, 0);

    cout << distance << endl;

    delete[] x_list;
    delete[] y_list;

    return 0;
}
