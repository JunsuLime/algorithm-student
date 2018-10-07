#include <stdio.h>
#include <stdlib.h>

#define INIT_HEAP_SIZE 8
#define PARENT_IDX(x) (x - 1) / 2
#define LEFT_CHILD_IDX(x) 2 * x + 1
#define RIGHT_CHILD_IDX(x) 2 * x + 2

// Min heap struct
struct heap {
    unsigned long long *container;
    int length;  // logical length of heap
    int size;  // physical size of container
};

void heap_init(struct heap *h) {
    h->container = (unsigned long long*)malloc(sizeof(unsigned long long) * INIT_HEAP_SIZE);
    h->length = 0;
    h->size = INIT_HEAP_SIZE;
}

void __swap(unsigned long long *array, int i1, int i2) {
    unsigned long long tmp = array[i1];
    array[i1] = array[i2];
    array[i2] = tmp;
}

void heap_push(struct heap *h, unsigned long long e) {
    int idx, parent_idx;

    if (h->length == h->size) {
        h->size = h->size << 1;  // h->size = h->size * 2
        h->container = (unsigned long long*)realloc(h->container, sizeof(unsigned long long) * h->size);
    }
    h->container[h->length++] = e;

    idx = h->length - 1;
    parent_idx = PARENT_IDX(idx);
    while (h->container[parent_idx] > h->container[idx]) {
        __swap(h->container, parent_idx, idx);
        idx = parent_idx;
        parent_idx = PARENT_IDX(idx);
    }
}

unsigned long long heap_pop(struct heap *h) {
    int idx, left_idx, right_idx;
    unsigned long long min_val = h->container[0];
    --h->length;

    if (h->length == h->size >> 2) {  // h->length == h->size * 4
        h->size = h->size >> 1;   // h->size = h->size * 2
        h->container = (unsigned long long*)realloc(h->container, sizeof(unsigned long long) * h->size);
    }

    idx = 0;
    __swap(h->container, 0, h->length);
 
    while (1) {
        left_idx = LEFT_CHILD_IDX(idx);
        right_idx = RIGHT_CHILD_IDX(idx);

        // no place to go down
        if (!(left_idx < h->length) && !(right_idx >= h->length))
            break;

        // if left and right both available
        if (left_idx < h->length && right_idx < h->length) {
            // choose smaller one and swap it
            if (h->container[idx] > h->container[left_idx] 
                && h->container[idx] > h->container[right_idx]) {
                if (h->container[left_idx] > h->container[right_idx]) {
                    __swap(h->container, idx, right_idx);
                    idx = right_idx;
                    continue;
                }
                else {
                    __swap(h->container, idx, left_idx);
                    idx = left_idx;
                    continue;
                }
            }
        }

        // if only left is available and current is bigger than left
        if (left_idx < h->length && h->container[idx] > h->container[left_idx]) {
            __swap(h->container, idx, left_idx);
            idx = left_idx;
            continue;
        }

        // if only right is available and current is bigger than right
        if (right_idx < h->length && h->container[idx] > h->container[right_idx]) {
            __swap(h->container, idx, right_idx);
            idx = right_idx;
            continue;
        }

        break;
    }
    return min_val;
}

void heap_free(struct heap *h) {
    free(h->container);
}

int heap_empty(struct heap *h) {
    return h->length == 0;
}

// for test
void heap_print(struct heap *h) {
    int i;
    for (i = 0; i < h->length; i++) {
        printf("%llu ", h->container[i]);
    }
    printf("\n");
}

int main() {
    int k, n;
    unsigned long long *array;
    struct heap heap;
    unsigned long long curr;
    int count = 0;
    int i = 0;

    scanf("%d %d", &k, &n);
    array = (unsigned long long*)malloc(sizeof(unsigned long long) * k);

    heap_init(&heap);
    for (i = 0; i < k; i++) {
        scanf("%llu", &array[i]);
        heap_push(&heap, array[i]);
    }

    while (!heap_empty(&heap)) {
        curr = heap_pop(&heap);

        if (++count == n)
            break;

        for (i = 0; i < k; i++) {
            heap_push(&heap, array[i] * curr);
            if (curr % array[i] == 0)
                break;
        }
    }
    heap_free(&heap);
    free(array);

    printf("%llu\n", curr);
    return 0;
}
