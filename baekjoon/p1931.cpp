#include <iostream>
#include <utility>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int n;
    cin >> n;

    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > queue;
    
    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;
        queue.push(pair<int, int>(end, start));
    }

    int count = 0;
    int curr = -1;
    while (!queue.empty()) {
        pair<int, int> p = queue.top();
        queue.pop();
        // first - end, second - start
        if (p.second >= curr) {
            curr = p.first;
            count++;
        }
    }

    cout << count << endl;
}
