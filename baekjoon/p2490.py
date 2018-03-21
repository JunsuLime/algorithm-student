for _ in range(3):
	a = list(map(int, input().split()))
	c = sum(a)
	if c == 0:
		print('D')
	elif c == 1:
		print('C')
	elif c == 2:
		print('B')
	elif c == 3:
		print('A')
	elif c == 4:
		print('E')
