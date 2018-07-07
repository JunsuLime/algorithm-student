#include <stdio.h>
#include <set>

using namespace std;

int minValueInSet(set<int> *s) {
	return *(s->begin());
}

int maxValueInSet(set<int> *s) {
	return *(s->rbegin());
}

void solve() {
	int n;
	scanf("%d", &n);

	set<int> under_set;
	set<int> upper_set;

	int *arr = new int[n];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		upper_set.insert(arr[i]);
	}

	int count = 0;

	for (int i = 0; i < n; i++) {
		upper_set.erase(arr[i]);
		
		if ((under_set.empty() || maxValueInSet(&under_set) < arr[i])
			&& (upper_set.empty() || minValueInSet(&upper_set) > arr[i]))
			count++;
		
		under_set.insert(arr[i]);
	}
	printf("%d\n", count);
}

int main() {
	int test_case;
	scanf("%d", &test_case);

	for (int i = 0; i < test_case; i++) {
		printf("Case #%d\n", i+1);
		solve();
	}
	return 0;
}
