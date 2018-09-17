#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define PUSH '+'
#define POP '-'

#define EMPTY -1
#define INIT_VECTOR_SIZE 16

struct stack {
    int *arr;
    int top;
    int size;
};

void init_stack(struct stack *stack, int size) {
    stack->arr = (int*)malloc(sizeof(int) * size);
    stack->size = size;
    stack->top = EMPTY;
}

void push_stack(struct stack *stack, int e) {
    stack->arr[++stack->top] = e;
}

int top_stack(struct stack *stack) {
    return stack->arr[stack->top];
}

void pop_stack(struct stack *stack) {
    stack->top--;
}

int empty_stack(struct stack *stack) {
    return stack->top == EMPTY;
}

void release_stack(struct stack *stack) {
    free(stack->arr);
}

struct vector {
    int *arr;
    int length;
    int size;
};

void init_vector(struct vector *vector) {
    vector->arr = (int*)malloc(sizeof(int) * INIT_VECTOR_SIZE);
    vector->length = 0; // logical length
    vector->size = INIT_VECTOR_SIZE; // physical length
}

void add_vector(struct vector *vector, char e) {
    if (vector->length == vector->size) {
        vector->size = vector->size << 1;
        vector->arr = (int*)realloc(vector->arr, sizeof(int) * vector->size);
    }

    vector->arr[vector->length++] = e;
}

void foreach_vector(struct vector *vector, void (*function)(char e)) {
    int i;
    for (i = 0; i < vector->length; i++) {
        function(vector->arr[i]);
    }
}

void release_vector(struct vector *vector) {
    free(vector->arr);
}

void print_ln(char ch) {
    printf("%c\n", ch);
}

int main() {
    int n, i;
    int *array;

    scanf("%d", &n);

    array = (int*)malloc(sizeof(int) * n);
    for (i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    struct stack stack;
    struct vector vector;

    init_stack(&stack, n);
    init_vector(&vector);

    int top;
    int curr = 0; // current referenced index in array

    for (i = 1; i <= n; i++) {
        push_stack(&stack, i);
        add_vector(&vector, PUSH);

        while (!empty_stack(&stack)) {
            top = top_stack(&stack);
            if (top != array[curr])
                break;

            curr++;
            pop_stack(&stack);
            add_vector(&vector, POP);
        }
    }

    // Impossible case
    if (curr != n) {
        printf("NO\n");
        return 0;
    }

    foreach_vector(&vector, print_ln);

    release_stack(&stack);
    release_vector(&vector);

    return 0;
}
