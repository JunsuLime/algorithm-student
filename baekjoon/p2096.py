import sys

n = int(sys.stdin.readline())

max_current = list(map(int, sys.stdin.readline().split()))
min_current = max_current[:]

for _ in range(n-1):
	line = list(map(int, sys.stdin.readline().split()))

	tmp_max = max_current[:]
	tmp_min = min_current[:]

	max_current[0] = max(tmp_max[0], tmp_max[1]) + line[0]
	max_current[1] = max(tmp_max) + line[1]
	max_current[2] = max(tmp_max[1], tmp_max[2]) + line[2]
	
	min_current[0] = min(tmp_min[0], tmp_min[1]) + line[0]
	min_current[1] = min(tmp_min) + line[1]
	min_current[2] = min(tmp_min[1], tmp_min[2]) + line[2]

sys.stdout.write('%d %d\n' % (max(max_current), min(min_current)))
