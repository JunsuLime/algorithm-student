#include <vector>
#include <algorithm>

#define MAX_FOOD 100000001

int solution(vector<int> foodTimes, long long k) {
    int prevLoop = 0;
    int currLoop = 0;

    int remainFood = 0;
    while (true) {
        vector<int>::iterator foodIter = foodTimes.begin();
        for (foodIter; foodIter != foodTimes.end(); ++foodIter) {
            if (*foodIter > prevLoop) {
                remainFood++;
                currLoop = min(currLoop, *foodIter);
            }
        }

        if (remainFood == 0) {
            return -1;
        }
        
        long long expected = k - (currLoop - prevLoop) * remainFood;
        if (expected < 0) {
            k = k % remainFood;
            break;
        }

        k = expected;
        prevLoop = currLoop;
        currLoop = MAX_FOOD;
    }

    for (int i = 0; i < foodTimes.size(); i++) {
        if (foodTimes[i] > prevLoop) {
            if (k == 0)
                return i+1;
            k--;
    }

    return -1;
}
