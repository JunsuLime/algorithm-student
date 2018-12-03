#include <stdio.h>
#include <algorithm>

#define TURN_G 0
#define TURN_M 1
#define UNDEFINED -1

#define MAX_IDX 1000

#define CHANGE_TURN(t) t == TURN_G ? TURN_M : TURN_G

using namespace std;

int cache[MAX_IDX + 1][MAX_IDX + 1][2];

void clean_cache() {
    for (int i = 0; i < MAX_IDX + 1; i++) {
        for (int j = 0; j < MAX_IDX + 1; j++) {
            cache[i][j][TURN_G] = UNDEFINED;
            cache[i][j][TURN_M] = UNDEFINED;
        }
    }
}

pair<int, int> score_cards(int *cards, int left, int right, int turn) {
    if (left > right)
        return make_pair(0, 0);

    if (cache[left][right][TURN_G] != UNDEFINED && cache[left][right][TURN_M] != UNDEFINED) {
        return make_pair(cache[left][right][TURN_G], cache[left][right][TURN_M]);
    }

    pair<int, int> left_scores = score_cards(cards, left + 1, right, CHANGE_TURN(turn));
    if (turn == TURN_G)
        left_scores.first += cards[left];
    else
        left_scores.second += cards[left];

    pair<int, int> right_scores = score_cards(cards, left, right - 1, CHANGE_TURN(turn));
    if (turn == TURN_G)
        right_scores.first += cards[right];
    else
        right_scores.second += cards[right];

    if (turn == TURN_G && left_scores.first > right_scores.first) {
        cache[left][right][TURN_G] = left_scores.first;
        cache[left][right][TURN_M] = left_scores.second;
        // printf("left = %d, right = %d, turn = %d, score = (%d, %d)\n", left, right, turn, left_scores.first, left_scores.second);
        return left_scores;
    }

    if (turn == TURN_M && left_scores.second > right_scores.second) {
        cache[left][right][TURN_G] = left_scores.first;
        cache[left][right][TURN_M] = left_scores.second;
        // printf("left = %d, right = %d, turn = %d, score = (%d, %d)\n", left, right, turn, left_scores.first, left_scores.second);
        return left_scores;
    }

    cache[left][right][TURN_G] = right_scores.first;
    cache[left][right][TURN_M] = right_scores.second;
    // printf("left = %d, right = %d, turn = %d, score = (%d, %d)\n", left, right, turn, right_scores.first, right_scores.second);
    return right_scores;
}

void solve() {
    int n;
    scanf("%d", &n);

    int cards[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &cards[i]);
    }

    clean_cache();

    // gnu first, not greedy but very clever
    // use dynamic programming
    printf("%d\n", score_cards(cards, 0, n-1, TURN_G).first);
}

int main() {
    int test_case;
    scanf("%d", &test_case);

    for (int i = 0; i < test_case; i++) {
        solve();
    }
    return 0;
}
