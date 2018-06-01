#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int n, tmp;
    cin >> n;

    priority_queue<int> queue;

    for (int i = 0; i < n; i++) {
        cin >> tmp;
        queue.push(tmp);
    }
    
    long total = 0;
    int i = 1;
    while (!queue.empty()) {
        total += queue.top() * i;
        queue.pop();
        i++;
    }
    cout << total << endl;
}   
