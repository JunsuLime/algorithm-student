a = int(input())
b = int(input())
c = int(input())

r = a * b * c
r = str(r)

for i in range(10):
	print(r.count(str(i)))
