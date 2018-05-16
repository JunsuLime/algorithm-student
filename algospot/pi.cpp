#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

using namespace std;

int score(int* l, int start, int end) {
    bool h1, h2, h3, h4;
    h1 = h2 = h3 = h4 = true;

    int prev = l[start];
    int jump = l[start+1] - l[start];

    for (int i = start+1; i < end; i++) {
        if (prev != l[i]) {
            h1 = false;
        }
        if (l[i]-prev != jump) {
            h2 = false;
            h4 = false;
        }
        if (i-2 >= start) {
            h3 &= l[i-2] == l[i];
        }
        if (i+2 < end) {
            h3 &= l[i+2] == l[i];
        }
        prev = l[i];
    }

    // cout << "start: " << start << " end: " << end << endl;
    // cout << "h1: " << h1 << " h2: " << h2 << " h3: " << h3 << " h4: " << h4 << " jump: " << jump << endl;
    if (h1) return 1;
    if (h2 && (jump == -1 || jump == 1)) return 2;
    if (h3) return 4;
    if (h4) return 5;
    
    return 10;
}

void work() {
    string pi;
    cin >> pi;

    int *digits = (int*) malloc(sizeof(int)*pi.size());
    for (int i = 0; i < pi.size(); i++) {
        digits[i] = (int) pi[i] - 48;
    }
    int *hard_score = (int*) malloc(sizeof(int)*(pi.size()+1));
    memset(hard_score, 0x00, sizeof(int)*(pi.size()+1));

    // 3, 4, 5
    for (int i = 3; i < 6; i++) {
        hard_score[i] = score(digits, 0, i);
    }

    for (int i = 3; i < pi.size(); i++) {
        // 3, 4, 5
        for (int j = 3; j < 6; j++) {
            if (i+j > pi.size()) {
                continue;
            }

            if (hard_score[i+j] == 0) {
                hard_score[i+j] = hard_score[i] + score(digits, i, i+j);

            }
            else {
                hard_score[i+j] = min(hard_score[i+j], hard_score[i] + score(digits, i, i+j));
            }
        }
    }

    cout << hard_score[pi.size()] << endl;
    free(hard_score);
}

int main() {
    int test_case;
    cin >> test_case;

    for (int i = 0; i < test_case; i++) {
        work();
    }

    return 0;
}
