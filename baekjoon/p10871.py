import sys

n, x = map(int, input().split())

for e in map(int, input().split()):
	if e < x:
		sys.stdout.write(str(e) + " ")
