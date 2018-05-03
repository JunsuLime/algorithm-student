# Topological sort with queue
#
# set degree and targets of each nodes
# 1) enqueue 0 degree nodes on queue
# 2) dequeue elements and reduce targets degree.
#    if target's degree is 0 -> enqueue target on queue.
#    loop this procedure
#    current ref item is appended on saved list
# 3) Do it until queue is empty! -> then in saved list , topological sorted items 
#    are there !! wow

import sys
from collections import deque

n, m = map(int, input().split())

# for 1 ~ n
visited = [False for _ in range(n+1)]

class Node(object):
	def __init__(self):
		self.targets = list()
		self.degree = 0

	def __repr__(self):
		return str(self.targets) + ' ' + str(self.degree)

# save nodes egde as adjacent list
graph = [Node() for _ in range(n+1)]

for _ in range(m):
	source, target = map(int, sys.stdin.readline().split())
	graph[source].targets.append(target)
	graph[target].degree += 1
	
q = deque()
l = list()

for i in range(1, len(graph)):
	if graph[i].degree == 0:
		q.append(i)


while len(q) != 0:
	cur = q.popleft()

	for t in graph[cur].targets:
		graph[t].degree -= 1
		if graph[t].degree == 0:
			q.append(t)

	l.append(cur)
	graph[cur] = None

for e in l:
	sys.stdout.write('%d ' % e)
sys.stdout.write('\n')
