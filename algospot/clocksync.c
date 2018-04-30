/* Time Complexity: O(4^10)
 * elapsed time: 528ms
 * 
 * Recusion, Complete Search
 * TODO: When problem needs lots of recursion, do not use python.
 * instead using C or C++. So familiar with C family.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

#define SWITCH_LEN 10
#define CLOCK_LEN 16

#define INVALID_CLICK 31
#define ROTATE 4


struct Switch {
	int *clocks;
	int len;
};

struct Switch* s_list;
int clocks[CLOCK_LEN];

// check clock is synchronized
int clock_sync_done() {
	int i;
	for (i = 0; i < CLOCK_LEN; i++) {
		if (clocks[i] != 0)
			return FALSE;
	}
	return TRUE;
}

// get click count in current clock state
// cur is current referenced clock index
int click_count(int cur) {
	// if clock is synchronized, do not need click button
	// so, return 0
	if (clock_sync_done()) {
		return 0;
	}
	// if cur refers invalid switch index
	// then, return INVALID_CLICK
	if (cur == SWITCH_LEN) {
		return INVALID_CLICK;
	}
	
	int count = INVALID_CLICK;
	int comp_count;
	int i, j;

	// for all rotations, check min count
	for (i = 0; i < ROTATE; i++) {
		struct Switch s = s_list[cur];	
		comp_count = click_count(cur+1) + i;
		if (count > comp_count)
			count = comp_count;
		
		// push botton
		for (j = 0; j < s.len; j++) {
			clocks[s.clocks[j]] = (clocks[s.clocks[j]] + 1) % ROTATE;	
		}
	}
	return count;
}

int work() {
	int i;
	int tmp;
	for (i = 0; i < CLOCK_LEN; i++) {
		scanf("%d", &tmp);
		if (tmp == 12)
			clocks[i] = 0;
		else
			clocks[i] = tmp / 3;
	}

	int click = click_count(0);
	if (click == INVALID_CLICK)
		return -1;
	else
		return click;
}

int main() {
	int test_case;
	
	// initial settings for switch
	int s0[3] = {0, 1, 2};
	int s1[4] = {3, 7, 9, 11};
	int s2[4] = {4, 10, 14, 15};
	int s3[5] = {0, 4, 5, 6, 7};
	int s4[5] = {6, 7, 8, 10, 12};
	int s5[4] = {0, 2, 14, 15};
	int s6[3] = {3, 14, 15};
	int s7[5] = {4, 5, 7, 14, 15};
	int s8[5] = {1, 2, 3, 4, 5};
	int s9[5] = {3, 4, 5, 9, 13};

	s_list = (struct Switch*) malloc(sizeof(struct Switch)*SWITCH_LEN);
	
	s_list[0].clocks = s0;
	s_list[0].len = 3;
	s_list[1].clocks = s1;
	s_list[1].len = 4;
	s_list[2].clocks = s2;
	s_list[2].len = 4;
	s_list[3].clocks = s3;
	s_list[3].len = 5;
	s_list[4].clocks = s4;
	s_list[4].len = 5;
	s_list[5].clocks = s5;
	s_list[5].len = 4;
	s_list[6].clocks = s6;
	s_list[6].len = 3;
	s_list[7].clocks = s7;
	s_list[7].len = 5;
	s_list[8].clocks = s8;
	s_list[8].len = 5;
	s_list[9].clocks = s9;
	s_list[9].len = 5;

	scanf("%d\n", &test_case);

	int i;
	for (i = 0; i < test_case; i++) {
		printf("%d\n", work());
	}

	return 0;
}
