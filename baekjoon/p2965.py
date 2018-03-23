a, b, c = map(int, input().split())

left = b - a
right = c - b

if left == 1 and right == 1:
	print(0)
	exit(0)

if left > right:
	c = a + 1
	r = b - c
else:
	a = c - 1
	r = a - b
print(r)

