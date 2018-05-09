#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

double geo_seq_sum(double a, double r, int n) {
	return (a * (1 - pow(r, n))) / (1 - r);
}	


double work() {
	int n, redip;
	scanf("%d", &n);
	scanf("%d", &redip);

	int dip = redip + 1;
	vector<int> num_list;
	for (int i = 0; i < n; i++) {
		int item;
		scanf("%d", &item);
		num_list.push_back(item);
	}
	num_list.resize(n);
	sort(num_list.begin(), num_list.end(), greater<int>());

	double expected_value = 0;

	int idx = 0;
	int cur, cur_count;
	cur = num_list[0];
	cur_count = 0;
	while (1) {
		if (idx == n) {
			return cur;
		}

		printf("idx: %d, n: %d, cur: %d, num: %d\n", idx, n, cur, num_list[idx]);
		if (cur > num_list[idx]) {
			double prob = (double)cur_count / (double)n;
			double pick_other_prob = (double)(n-idx) / (double)n;
			double g_sum = geo_seq_sum(prob, pick_other_prob, dip);
			expected_value += cur * g_sum;
			printf("cur: %d, g_sum: %f\n", cur, g_sum);
			break;
		}
		else {
			cur_count++;
			idx++;
		}
	}

	cur = num_list[idx];
	cur_count = 0;
	for (int i = idx; i < n+1; i++) {
		if (i == n) {
			double p1 = pow((double)cur_count / (double)n, dip);
			printf("cur: %d, p1: %f\n", cur, p1);
			expected_value += cur * p1;
		}
		else if (cur > num_list[i]) {
			double p1 = pow((double)(n-(i-cur_count)) / (double)n, dip);
			double p2 = pow((double)(n-i) / (double)n, dip);

			printf("cur: %d, p1-p2: %f\n", cur, p1-p2);	
			expected_value += cur * (p1 - p2);
			cur = num_list[i];
			cur_count = 1;
		}
		else {
			cur_count++;
		}
	}

	return expected_value;
}

int main() {
	int test_case;
	scanf("%d\n", &test_case);
	for (int i = 0; i < test_case; i++) {
		printf("Case #%d: %f\n", i+1, work());
	}

	return 0;
}
