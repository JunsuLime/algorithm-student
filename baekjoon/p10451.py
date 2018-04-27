import sys

test_case = int(sys.stdin.readline())

VISITED = 0
NOT_VISITED = 1

def work():
	n = int(sys.stdin.readline())

	g_map = [list() for _ in range(n)]
	for i, e in enumerate(map(int, sys.stdin.readline().split())):
		g_map[i].append(e-1)
	
	visited = [NOT_VISITED for _ in range(n)]
	v_s = set(range(n))
	visit_count = 0
	count = 0

	def get_not_visited_node():
		for e in v_s:
			return e
		return None

	while visit_count < n:
		cur = get_not_visited_node()
		stack = list()

		visit_count += 1
		visited[cur] = VISITED
		v_s.remove(cur)
		stack.append(cur)
		while len(stack) != 0:
			cur = stack.pop()
			for b in g_map[cur]:
				if visited[b] == NOT_VISITED:
					visit_count += 1
					visited[b] = VISITED
					v_s.remove(b)
					stack.append(b)

		count += 1
	
	return count


for _ in range(test_case):
	print(work())
