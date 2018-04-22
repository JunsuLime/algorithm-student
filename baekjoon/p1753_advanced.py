import heapq
import sys


UNDEFINED = -1

vertex_num, edge_num = map(int, sys.stdin.readline().split())
start_point = int(sys.stdin.readline())
start_point -= 1

# in set - (end, weight) tuple is saved 
graph_map = [set() for _ in range(vertex_num)]
# [prev_node, distance] - short_way
short_way = [[UNDEFINED, UNDEFINED] for _ in range(vertex_num)]

for _ in range(edge_num):
	start, end, weight = map(int, sys.stdin.readline().split())
	graph_map[start-1].add((end-1, weight))

short_way[start_point][0] = start_point
short_way[start_point][1] = 0

heap = list()
heapq.heappush(heap, (0, start_point))

while len(heap) != 0:
	distance, cur = heapq.heappop(heap)
	branches = graph_map[cur]

	if short_way[cur][1] < distance:
		continue

	for b in branches:
		end, weight = b
		if short_way[end][0] == UNDEFINED or short_way[end][1] > distance + weight:
			short_way[end][0] = cur
			short_way[end][1] = distance + weight
			heapq.heappush(heap, (short_way[end][1], end))

for s in short_way:
	if s[1] == UNDEFINED:
		sys.stdout.write('INF\n')
	else:
		sys.stdout.write('%d\n' % s[1])
