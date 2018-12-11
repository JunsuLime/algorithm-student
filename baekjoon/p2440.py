import sys

n = int(sys.stdin.readline())
for i in range(n, 0, -1):
    sys.stdout.write('*' * i)
    sys.stdout.write('\n')
