n = int(input())

# memoization dynamic programming

l = [-1 for _ in range(n+1)]
l[1] = 0

for i in range(2, n+1):
	c = l[i-1]
	if i % 2 == 0:
		# shift >> 1 is same as / 2 calc
		c = min(c, l[i >> 1])
	if i % 3 == 0:
		c = min(c, l[int(i/3)])
	
	# print(l, i, c)
	l[i] = c + 1

# print(l)
print(l[len(l) - 1])

