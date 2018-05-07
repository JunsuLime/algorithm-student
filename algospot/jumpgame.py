import sys

test_case = int(sys.stdin.readline())

def print_output(output):
	if output:
		print('YES')
	else:
		print('NO')

def work():
	n = int(sys.stdin.readline())
	ground = list()

	for i in range(n):
		ground.append(list(map(int, sys.stdin.readline().split())))

	# possible in x, y 2d-array - cache in Dynamic Programming
	possible = [[False for _ in range(n)] for _ in range(n)]

	# DFS search
	s = list()
	s.append((0, 0))

	while s:
		x, y = s.pop()
		if x == n-1 and y == n-1:
			return True

		d = ground[x][y]
		if x+d < n and not possible[x+d][y]:
			possible[x+d][y] = True
			s.append((x+d, y))
		if y+d < n and not possible[x][y+d]:
			possible[x][y+d] = True
			s.append((x, y+d))

	# reachable on end point
	return possible[n-1][n-1]

for _ in range(test_case):
	print_output(work())
