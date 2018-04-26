import sys
from collections import deque

n = int(sys.stdin.readline())

g_map = [list() for _ in range(n+1)]
for _ in range(n-1):
	p1, p2 = map(int, sys.stdin.readline().split())
	g_map[p1].append(p2)
	g_map[p2].append(p1)

# first build tree with adjacent list
# traverse and get node's parent 
# Because python3 have limittation of recursion, traverse with BFS
# print node's parent

q = deque()
q.append(1)

p_saver = [0 for _ in range(n+1)]

visited = set()

while len(q) != 0:
	cur = q.popleft()
	for b in g_map[cur]:
		if b in visited:
			continue
		p_saver[b] = cur
		visited.add(b)
		q.append(b)

for i in range(2, len(p_saver)):
	print(p_saver[i])


