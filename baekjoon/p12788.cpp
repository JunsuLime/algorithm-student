#include <iostream>
#include <queue>

using namespace std;

int main() {
    priority_queue<int> queue;
    int n, m, k, tmp;
    cin >> n >> m >> k;

    int total_pen_cnt = 0;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        total_pen_cnt += tmp;
        queue.push(tmp);
    }

    int needed_pen_cnt = m * k;
    if (needed_pen_cnt > total_pen_cnt) {
        cout << "STRESS" << endl;
        return 0;
    }

    int borrow_cnt = 0;
    while (!queue.empty() && needed_pen_cnt > 0) {
        needed_pen_cnt -= queue.top();
        queue.pop();

        borrow_cnt++;
    }

    cout << borrow_cnt << endl;
    return 0;
}
