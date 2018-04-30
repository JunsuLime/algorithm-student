/**
 * Time Complexity: O(nlogn)
 * Elasped time: 56ms
 *
 * python is bad for recursion .. use C.
 * Divide and Conquer problem amazing solution
 */

#include <stdio.h>
#include <stdlib.h>

// get max_rect between left and right
int max_rect(int *fence, int left, int right) {
	if (right - left == 1) {
		return fence[left];
	}	

	// mid = (left + right) / 2
	int mid = (left+right) >> 1;

	int m_rect, cmp_rect;
	
	// half-opened range [)
	// CASE 1: max rect is on only left part or right part
	m_rect = max_rect(fence, left, mid);
	cmp_rect = max_rect(fence, mid, right);
	
	// update with max rect value
	if (cmp_rect > m_rect) 
		m_rect = cmp_rect;
	
	int ref_left, ref_right, height, cmp_height;
	ref_left = mid;
	ref_right = mid;

	height = fence[ref_left] < fence[ref_right] ? fence[ref_left] : fence[ref_right];

	// CASE 2: max rect appear along left and right side both.
	while (1) {
		cmp_rect = (ref_right - ref_left + 1) * height;
		if (cmp_rect > m_rect) 
			m_rect = cmp_rect;

		// if left and right both can be expaneded
		if (left <= ref_left-1 && ref_right+1 < right) {
			if (fence[ref_left-1] > fence[ref_right+1]) {
				ref_left--;
				cmp_height = fence[ref_left];
			}
			else {
				ref_right++;
				cmp_height = fence[ref_right];
			}
		}
		// if only left can be expanded
		else if (left <= ref_left-1) {
			ref_left--;
			cmp_height = fence[ref_left];
		}
		// if only right can be expanded
		else if (ref_right+1 < right) {
			ref_right++;
			cmp_height = fence[ref_right];
		}
		else {
			break;
		}

		// get min height value
		if (cmp_height < height) {
			height = cmp_height;
		}
	}
	return m_rect;
}

int work() {
	int fence_count;
	scanf("%d\n", &fence_count);

	int *fence = (int*) malloc(sizeof(int)*fence_count);
	int i;
	for (i = 0; i < fence_count; i++) {
		scanf("%d", &fence[i]);
	}

	return max_rect(fence, 0, fence_count);
}

int main() {
	int test_case;

	scanf("%d\n", &test_case);
	int i;
	for (i = 0; i < test_case; i++) {
		printf("%d\n", work());
	}
}
