#include <stdio.h>
#include <string.h>

#define GEAR_INFO_LEN 8
#define NUM_GEAR 4

#define CLOCKWISE 1
#define COUNTER_CLOCKWISE -1

#define TOP_MASK 0b10000000
#define LAST_MASK 0b00000001

#define LEFT_MASK 0b00000010
#define RIGHT_MASK 0b00100000
#define TRIM_MASK 0b11111111

void print_gear(int gear) {
    int i;
    int mask = TOP_MASK;
    for (i = 0; i < GEAR_INFO_LEN; i++) {
        printf("%d", (gear & mask) != 0);
        mask >>= 1;
    }
    printf("\n");
}

void init_gear(int *gear, char *gear_info) {
    int i;
    *gear = 0;
    for (i = 0; i < GEAR_INFO_LEN; i++) {
        if (gear_info[i] == '0')
            continue;
        *gear |= 1 << (GEAR_INFO_LEN - 1 - i);
    }
}

void rotate_gear(int *gear, int direction) {
    int rotated;
    if (direction == CLOCKWISE) {
        rotated = (*gear & LAST_MASK) != 0;
        *gear >>= 1;
        *gear |= rotated << (GEAR_INFO_LEN - 1);
        return;
    }

    rotated = (*gear & TOP_MASK) != 0;
    *gear <<= 1;
    *gear &= TRIM_MASK;
    *gear |= rotated;
}

int is_left_rotatable(int prev, int curr) {
    int prev_state = (prev & LEFT_MASK) == 0;
    int curr_state = (curr & RIGHT_MASK) == 0;

    return prev_state != curr_state;
}

int is_right_rotatable(int prev, int curr) {
    int prev_state = (prev & RIGHT_MASK) == 0;
    int curr_state = (curr & LEFT_MASK) == 0;

    return prev_state != curr_state;
}

void rotate_gears(int gears[NUM_GEAR], int start, int direction) {
    // First, check rotate directions.
    // Second, rotate gears.
    int rotate_info[NUM_GEAR];
    int prev_gear;
    int gear_idx, curr_dir, i;

    memset(rotate_info, 0x00, sizeof(int) * NUM_GEAR);
    
    // left side rotate
    curr_dir = direction;
    gear_idx = start - 1;
    while (gear_idx >= 0) {
        prev_gear = gears[gear_idx + 1];
        if (!is_left_rotatable(prev_gear, gears[gear_idx]))   
            break;
        
        curr_dir = curr_dir == CLOCKWISE ? COUNTER_CLOCKWISE : CLOCKWISE;
        rotate_info[gear_idx] = curr_dir;
        gear_idx--;
    }
    for (i = start - 1; i >= 0; i--) {
        if (rotate_info[i] == 0)
            break;

        rotate_gear(&gears[i], rotate_info[i]);
    } 
    
    // right side rotate
    curr_dir = direction;
    gear_idx = start + 1;
    while (gear_idx < NUM_GEAR) {
        prev_gear = gears[gear_idx - 1];
        if (!is_right_rotatable(prev_gear, gears[gear_idx]))
            break;
        
        curr_dir = curr_dir == CLOCKWISE ? COUNTER_CLOCKWISE : CLOCKWISE;
        rotate_info[gear_idx] = curr_dir;
        gear_idx++;
    }
    for (i = start + 1; i < NUM_GEAR; i++) {
        if (rotate_info[i] == 0)
            break;
        
        rotate_gear(&gears[i], rotate_info[i]);
    }

    // start gear rotate
    rotate_gear(&gears[start], direction);
}

int score_gear(int gears[NUM_GEAR]) {
    int i;
    int score = 0;

    for (i = 0; i < NUM_GEAR; i++) {
        if ((gears[i] & TOP_MASK) == 0)
            continue;
        score += 1 << i;
    }
    return score;
}

int main() {
    int gears[NUM_GEAR];
    char gear_info[GEAR_INFO_LEN + 1];
    
    int num_rotate;
    int i, start, direction;

    for (i = 0; i < NUM_GEAR; i++) {
        scanf("%s", gear_info);
        init_gear(&gears[i], gear_info);
    }
    
    scanf("%d", &num_rotate);
    for (i = 0; i < num_rotate; i++) {
        scanf("%d %d", &start, &direction);
        rotate_gears(gears, start - 1, direction);
    }

    printf("%d\n", score_gear(gears));
}
