import sys

n = int(input())

for i in range(1, n+1):
	for _ in range(i):
		sys.stdout.write('*')
	sys.stdout.write('\n')

