#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* cache;

int lis(int* arr, int len, int cur) {
	if (cache[cur] != 0) {
		return cache[cur];
	}

	int i = 0;
	int max_val = 0;
	int val;

	for (i = cur+1; i < len; i++) {
		if (arr[i] > arr[cur]) {
			val = lis(arr, len, i) + 1;
			if (val > max_val) {
				max_val = val;
			}
		}
	}
	
	cache[cur] = max_val;
	return max_val;
}

void work() {
	int n;
	scanf("%d\n", &n);

	cache = (int*) malloc(sizeof(int)*n);
	memset(cache, 0x00, sizeof(int)*n);
	int *arr = (int*) malloc(sizeof(int)*n);

	int i;
	for (i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	int max_val = 0;
	int val;
	for (i = 0; i < n; i++) {
		val = lis(arr, n, i) + 1;
		if (val > max_val) {
			max_val = val;
		}	
	}

	free(cache);
	printf("%d\n", max_val);
}

int main() {
	int test_case;
	scanf("%d\n", &test_case);

	int i;
	for (i = 0; i < test_case; i++) {
		work();
	}

	return 0;
}
