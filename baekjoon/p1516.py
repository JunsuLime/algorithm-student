import sys
import heapq
from collections import deque

class Node(object):
	def __init__(self):
		self.targets = list()
		self.self_time = 0
		self.total_time = 0
		self.degree = 0

class MinHeap(object):
	def __init__(self):
		self.h = list()
	
	def push(self, t, e):
		heapq.heappush(self.h, (t, e))
	
	def pop(self):
		return heapq.heappop(self.h)
	
	def __len__(self):
		return len(self.h)


s_num = int(input())

# 1 ~ n
graph = [Node() for _ in range(s_num+1)]
h = MinHeap()

for i in range(1, s_num+1):
	d = 0
	for idx, e in enumerate(map(int, sys.stdin.readline().split())):
		if e == -1:
			continue
		if idx == 0:
			graph[i].self_time = e
			graph[i].total_time = e
		else:
			graph[e].targets.append(i)
			d += 1
	
	graph[i].degree = d
	if d == 0:
		h.push(graph[i].total_time, i)

while len(h) != 0:
	time, cur = h.pop()
	
	for b in graph[cur].targets:
		graph[b].degree -= 1
		if graph[b].degree == 0:
			if time + graph[b].self_time > graph[b].total_time:
				graph[b].total_time = time + graph[b].self_time
				h.push(graph[b].total_time, b)

for i in range(1, len(graph)):
	sys.stdout.write('%d\n' % graph[i].total_time)

