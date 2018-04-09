def giyakboonsoo(children, mother):
	gcd_val = gcd(children, mother)
	return "%d/%d" % (children // gcd_val, mother // gcd_val)

def gcd(a, b):
	divided_val = max(a, b)
	divider = min(a, b)

	while True:
		remainder = divided_val % divider
		if remainder == 0:
			return divider

		divided_val = divider
		divider = remainder

num_ring = int(input())

rings = list(map(int, input().split()))

for i in range(1, len(rings)):
	print(giyakboonsoo(rings[0], rings[i]))

