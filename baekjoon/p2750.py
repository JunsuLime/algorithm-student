import sys

n = int(sys.stdin.readline())
l = list()
for _ in range(n):
	l.append(int(sys.stdin.readline()))

l.sort()
for e in l:
	sys.stdout.write('%d\n' % e)

