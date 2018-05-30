/**
 * LunchBox Problem
 * 
 * total_time = sum(wave) + alpha == max(all people's (begin + eat_time))
 * so, eat_time descending sort!
 *
 * prove ... make optimal answer with eat_time descending order by non descending order answer
 *
 * OK - it can be made
 */

#include <iostream>
#include <stdlib.h>
#include <algorithm>

using namespace std;

struct Lunch {
    int wave;
    int eat;

    bool operator< (Lunch l) const {
        return eat < l.eat;
    }
    bool operator> (Lunch l) const {
        return eat > l.eat;
    }   
};

void work() {
    int n;
    cin >> n;

    int tmp;
    int elapsed = 0;
    int time_stack = 0;

    Lunch *l = (Lunch*) malloc(sizeof(Lunch)*n);

    for (int i = 0; i < n; i++) {
        cin >> tmp;
        l[i].wave = tmp;
    }

    for (int i = 0; i < n; i++) {
        cin >> tmp;
        l[i].eat = tmp;
    }

    // sort by descending order
    sort(l, l+n, greater<Lunch>());
    for (int i = 0; i < n; i++) {
        time_stack += l[i].wave;
        elapsed = max(elapsed, time_stack+l[i].eat);
    }

    cout << elapsed << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    
    int test_case;
    cin >> test_case;

    for (int i = 0; i < test_case; i++) {
        work();
    }
}
