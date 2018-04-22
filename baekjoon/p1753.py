from collections import deque

UNDEFINED = -1

vertex_num, edge_num = map(int, input().split())
start_point = int(input())
start_point -= 1

# in set - (end, weight) tuple is saved 
graph_map = [set() for _ in range(vertex_num)]
# [prev_node, distance] - short_way
short_way = [[UNDEFINED, UNDEFINED] for _ in range(vertex_num)]

for _ in range(edge_num):
	start, end, weight = map(int, input().split())
	graph_map[start-1].add((end-1, weight))

short_way[start_point][0] = start_point
short_way[start_point][1] = 0

queue = deque()
queue.append(start_point)

while len(queue) != 0:
	cur = queue.popleft()
	branches = graph_map[cur]

	for b in branches:
		end, weight = b
		if short_way[end][0] == UNDEFINED or short_way[end][1] > short_way[cur][1] + weight:
			short_way[end][0] = cur
			short_way[end][1] = short_way[cur][1] + weight
			queue.append(end)

for s in short_way:
	if s[1] == UNDEFINED:
		print('INF')
	else:
		print(s[1])
