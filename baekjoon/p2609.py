l = list(map(int, input().split()))

a = max(l)
b = min(l)

divided_val = a
divider = b

gcd = 1

while True:
	remainder = divided_val % divider

	if remainder == 0:
		gcd = divider
		break

	divided_val = divider
	divider = remainder

print(gcd)
print((a*b)//gcd)
