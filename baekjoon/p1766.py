import heapq
import sys


class Node(object):
	def __init__(self):
		self.targets = list()
		self.degree = 0

	def __repr__(self):
		return '%r %d' % (self.targets, self.degree)

num_problem, num_pair = map(int, sys.stdin.readline().rstrip().split())
graph = [Node() for _ in range(num_problem+1)]

for _ in range(num_pair):
	source, target = map(int, sys.stdin.readline().rstrip().split())
	graph[source].targets.append(target)
	graph[target].degree += 1

heap = list()
for i in range(1, num_problem+1):
	if graph[i].degree == 0:
		heapq.heappush(heap, i)

result = list()

while heap:
	cur = heapq.heappop(heap)
	result.append(cur)
	for b in graph[cur].targets:
		graph[b].degree -= 1
		if graph[b].degree == 0:
			heapq.heappush(heap, b)

for e in result:
	sys.stdout.write('%d ' % e)
sys.stdout.write('\n')
