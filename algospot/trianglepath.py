import sys

test_case = int(sys.stdin.readline())

def work():
	t_size = int(sys.stdin.readline())

	cache = list()
	cache.append(int(sys.stdin.readline()))

	for _ in range(t_size-1):
		line = list(map(int, sys.stdin.readline().split()))
		
		tmp = cache[:]
		cache[0] = line[0] + tmp[0]
		for i in range(1, len(tmp)):
			cache[i] = max(tmp[i-1], tmp[i]) + line[i]
		cache.append(tmp[-1] + line[-1])

	sys.stdout.write('%d\n' % max(cache))

for _ in range(test_case):
	work()
