import sys
num = int(sys.stdin.readline())

def print_output(s):
	sys.stdout.write('Hello, %s!\n' % s)

for _ in range(num):
	print_output(sys.stdin.readline().rstrip())

