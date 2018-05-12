#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <set>

#define STAR '*'
#define QUESTION '?'
#define SIZE 101
#define TRUE 1
#define FALSE 2
#define UNKNOWN 0

using namespace std;

int cached[SIZE][SIZE];

bool is_valid(string regexp, string filename, int r_idx, int f_idx) {
    
    bool result = false;
    
    if (r_idx == regexp.size() && f_idx == filename.size()) {
        result |= true;
    }
    else if (cached[r_idx][f_idx] != UNKNOWN) {
        return cached[r_idx][f_idx] == TRUE;
    }
    else if (f_idx == filename.size() && r_idx != regexp.size()) {
        if (regexp[r_idx] == STAR) {
            result |= is_valid(regexp, filename, r_idx+1, f_idx);
        }
        else {
            result |= false;   
        }
    }
    else if (regexp[r_idx] == STAR) {
        result |= is_valid(regexp, filename, r_idx, f_idx+1);
        result |= is_valid(regexp, filename, r_idx+1, f_idx);
    }
    else if (regexp[r_idx] == QUESTION) {
        result |= is_valid(regexp, filename, r_idx+1, f_idx+1);
    }
    else {
        if (regexp[r_idx] == filename[f_idx]) {
            result |= is_valid(regexp, filename, r_idx+1, f_idx+1);
        }
        else {
            result |= false;
        }
    }

    if (result) {
        cached[r_idx][f_idx] = TRUE;
    }
    else {
        cached[r_idx][f_idx] = FALSE;
    }
    return result;
}

void work() {
    string regexp;
    cin >> regexp;

    int file_num;
    cin >> file_num;

    set<string> s;

    for (int i = 0; i < file_num; i++) {
        string filename;
        cin >> filename;
        
        memset(cached, 0x00, sizeof(int)*SIZE*SIZE);
        if (is_valid(regexp, filename, 0, 0)) {
            s.insert(filename);
        }
    }

    set<string>::iterator iter;
    for (iter = s.begin(); iter != s.end(); iter++) {
        cout << *iter << endl;
    }
}

int main() {
    int test_case;

    cin >> test_case;

    for (int i = 0; i < test_case; i++) {
        work();
    }
}
