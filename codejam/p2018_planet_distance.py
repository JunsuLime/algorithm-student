import sys

test_case = int(input())

VISITED = 0
NOTYET = 1

def work(case_num):
    n = int(sys.stdin.readline())
    
    # adjacent list
    # 1 ~ n, 0 is not used
    graph = [list() for _ in range(n+1)]
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        # bidirectional
        graph[start].append(end)
        graph[end].append(start)

    cycle_set = set()   # cycle number set
    answers = [None for _ in range(n+1)]    # answers

    # Find cycle in graph
    stack_set = set()
    stack = list()
    visited = [NOTYET for _ in range(n+1)]

    cycle_starter = None

    # start from 1
    stack.append(1)
    stack_set.add(1)
    visited[1] = VISITED
    prev = None

    # preordering graph search with stack
    while stack:
        top = stack[len(stack)-1]
        for b in graph[top]:
            # if node is not parent and it is already visited set (in stack set)
            if len(stack) > 1 and stack[len(stack)-2] != b and b in stack_set:
                cycle_starter = b
                break
            if visited[b] == VISITED:
                continue

            stack.append(b)
            stack_set.add(b)
            visited[b] = VISITED
            break

        if cycle_starter:
            break
        if prev == top:
            stack.pop()
            stack_set.remove(top)
        
        prev = top

    cycle_start_idx = stack.index(cycle_starter)
    for i in range(cycle_start_idx, len(stack)):
        cycle_set.add(stack[i])
        answers[stack[i]] = 0   # in gift distance == 0

    # find each distance

    # 1) easy find answer by stack info
    for i in range(cycle_start_idx):
        answers[stack[i]] = cycle_start_idx - i

    # 2) search distance, planet id is started from 1
    for i in range(1, len(answers)):
        if answers[i] is not None:
            continue
        
        # reuse visited list
        for j in range(len(visited)):
            visited[j] = NOTYET
        
        prev = None
        stack = list()
        stack.append(i)
        visited[i] = VISITED

        cycle_found = False
        while stack:
            top = stack[len(stack)-1]
            for b in graph[top]:
                if b in cycle_set:
                    cycle_found = True
                    break
                # if b is parent node
                if visited[b] == VISITED:
                    continue
                stack.append(b)
                visited[b] = VISITED
                break

            if cycle_found:
                break
            if prev == top:
                stack.pop()

            prev = top
        
        # distance come out
        for idx, s_item in enumerate(stack):
            answers[s_item] = len(stack) - idx

    # print answer
    sys.stdout.write('Case #%d: ' % (case_num+1))
    for i in range(1, len(answers)):
        sys.stdout.write('%d ' % answers[i])
    sys.stdout.write('\n')

for i in range(test_case):
    work(i)
