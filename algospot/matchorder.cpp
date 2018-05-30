/**
 * Greedy Choice Property is very important!!
 * Prove it !!
 * 
 * In this problem
 * 1) cannot win with any member
 * 2) can win
 *
 * 1 - min member go can be optimal answer
 * 2 - min win member go can be optimal answer
 * So, greedy approach can be used
 */

#include <iostream>
#include <vector>
#include <set>

using namespace std;

void work() {
    vector<int> enemies;
    multiset<int> members;

    int m_num, tmp;
    cin >> m_num;

    for (int i = 0; i < m_num; i++) {
         cin >> tmp;
         enemies.push_back(tmp);
    }
    for (int i = 0; i < m_num; i++) {
         cin >> tmp;
         members.insert(tmp);
    }
    enemies.resize(m_num);
    
    int win_count = 0;
    vector<int>::iterator v_iter = enemies.begin();
    for (; v_iter != enemies.end(); v_iter++) {
        // cannot win with any member
        if (*members.rbegin() < *v_iter) {
            members.erase(members.begin());
        }
        else {
            multiset<int>::iterator s_iter = members.begin();
            for (; s_iter != members.end(); s_iter++) {
                if (*s_iter >= *v_iter) {
                    members.erase(s_iter);
                    win_count++;
                    break;
                }
            }
            // line 45 ~ 52 can be replaced by
            // members.erase(members.lower_bound(*v_iter));
            // win_count++;
        }
    }

    cout << win_count << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    
    int test_case;
    cin >> test_case;

    for (int i = 0; i < test_case; i++) {
        work();
    }
    return 0;
}
