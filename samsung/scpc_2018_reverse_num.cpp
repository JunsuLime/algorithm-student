#include <iostream>
#include <vector>
#include <algorithm>

#define ANSWER_NUM 3

using namespace std;

bool isReverseNumber(int number) {
    int tmp = number;
    int compare_num = 0;
    while (tmp) {
        compare_num = (compare_num * 10) + tmp % 10;
        tmp = tmp / 10;
    }

    return compare_num == number;
}

int *findCombination(int n, vector<int> *reverse_list) {
    vector<int> r_list = *reverse_list;
    int *answer_list = new int[ANSWER_NUM];
    for (int i = 0; i < ANSWER_NUM; i++) {
        answer_list[i] = 0;
    }

    int size = r_list.size();
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            for (int k = 0; k < size; k++) {
                if (n == r_list[i] + r_list[j] + r_list[k]) {
                    answer_list[0] = r_list[i];
                    answer_list[1] = r_list[j];
                    answer_list[2] = r_list[k];

                    sort(answer_list, answer_list + ANSWER_NUM, greater<int>());
                    return answer_list;
                }
            }
        }
    }
    return answer_list;
}

void solve() {
    int n;
    cin >> n;

    if (isReverseNumber(n)) {
        cout << 1 << " "  << n << endl;
        return;
    }

    vector<int> reverse_list;

    // include 0 - empty combination
    for (int i = 0; i < n; i++) {
        if (isReverseNumber(i)) {
            reverse_list.push_back(i);
        }
    }

    int *answer_list = findCombination(n, &reverse_list);
    int answer_cnt = 0;
    for (int i = 0; i < ANSWER_NUM; i++) {
        if (answer_list[i] != 0)
            answer_cnt++;
    }

    if (answer_cnt == 0) {
        cout << -1 << endl;
    }
    else {
        cout << answer_cnt << " ";
        for (int i = 0; i < answer_cnt; i++) {
            cout << answer_list[i] << " ";
        }
        cout << endl;
    }
    delete[] answer_list;
}

int main() {
    ios_base::sync_with_stdio(false);
    int test_case;
    cin >> test_case;

    for (int i = 0; i < test_case; i++) {
        cout << "Case #" << i+1 << endl;
        solve();
    }
    return 0;
}
