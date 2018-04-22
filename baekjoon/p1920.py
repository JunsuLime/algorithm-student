import sys

# python3's set is implemented  by hashtable
# so contain check time complexity O(1)

n = int(input())
s = set()
for e in map(int, input().split()):
	s.add(e)

_ = int(input())
for e in map(int, input().split()):
	if e in s:
		sys.stdout.write('1\n')
	else:
		sys.stdout.write('0\n')
