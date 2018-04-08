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


print((a*b) // gcd)
