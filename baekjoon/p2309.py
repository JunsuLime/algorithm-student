import itertools

pool = list()

for _ in range(9):
	pool.append(int(input()))

l_sum = sum(pool)
del_val = l_sum - 100

# find all combination made by 2 components
for i in range(8):
	for j in range(i+1, 9):
		if pool[i] + pool[j] == del_val:
			r1 = pool[i]
			r2 = pool[j]
			pool.remove(r1)
			pool.remove(r2)
			pool.sort()
			for p in pool:
				print(p)
			exit(0)

