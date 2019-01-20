#include <stdio.h>
#include <algorithm>

using namespace std;

class Conn {
public:
    int count;
    int target;
};

int main() {
    int n;
    scanf("%d", &n);
    
    // index 0 is sentinal node;
    Conn *connections = new Conn[n+1];
    for (int i = 1; i <= n; i++) {
        scanf("%d", &connections[i].target);
    }
    
    int max_conn = 0;
    connections[0].count = 0;
    connections[0].target = 0;
    for (int i = 1; i <= n; i++) {
        Conn *curr = &connections[i];
        Conn *candidate = &connections[0];
        for (int j = 1; j < i; j++) {
            Conn *compare = &connections[j];
            if (compare->target > curr->target) {
                continue;
            }
            if (compare->count > candidate->count) {
                candidate = compare;
            }
            else if (compare->count == candidate->count &&
                     compare->target < candidate->target) {
                candidate = compare;
            }
        }
        curr->count = candidate->count + 1;
        max_conn = max(max_conn, curr->count);
    }
    
    printf("%d\n", max_conn);
    return 0;
}

