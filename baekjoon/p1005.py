import sys
import heapq


class Node(object):
    def __init__(self):
        self.degree = 0
        self.next = list()
        self.b_time = 0

def work():
    b_num, r_num = map(int, sys.stdin.readline().rstrip().split())
    
    rules = [Node() for _ in range(b_num)]

    for i, t in enumerate(map(int, sys.stdin.readline().rstrip().split())):
        rules[i].b_time = t

    for _ in range(r_num):
        start, end = map(int, sys.stdin.readline().rstrip().split())

        # index is started from 0
        start -= 1
        end -= 1

        rules[start].next.append(end)
        rules[end].degree += 1

    # index is started from 0
    final_b = int(sys.stdin.readline())
    final_b -= 1

    heap = list()
    for n in rules:
        if n.degree == 0:
            heapq.heappush(heap, (n.b_time, n))

    final_b_time = 0

    while heap:
        node_time, node = heapq.heappop(heap)
        finished = False
        for n_idx in node.next:
            next_node = rules[n_idx]
            next_node.degree -= 1
            if next_node.degree == 0:
                next_node.b_time += node_time
                if n_idx == final_b:
                    final_b_time = next_node.b_time
                    finished = True
                    break
                heapq.heappush(heap, (next_node.b_time, next_node))
        if finished:
            break

    sys.stdout.write('%d\n' % final_b_time)


test_case = int(sys.stdin.readline())

for _ in range(test_case):
    work()
