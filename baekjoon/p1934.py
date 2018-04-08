test_case = int(input())

def work():
	"""
	solve by euclidean algorithm

	1) get gcd
	2) a * b = gcd * lcm
	3) lcm = a * b / gcd(a,b)
	"""
	l = list(map(int, input().split()))
	a = max(l)
	b = min(l)

	gcd = 1
	divided_val = a
	divider = b

	while True:
		remainder = divided_val % divider

		if remainder == 0:
			gcd = divider
			break

		divided_val = divider
		divider = remainder
	
	return (a * b) // gcd



for _ in range(test_case):
	print(work())
