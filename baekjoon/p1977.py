# find n ** 2 - number of n in [min, max]

import math

min_val = int(input())
max_val = int(input())

min_root = int(math.sqrt(min_val))
max_root = int(math.sqrt(max_val))

if min_root ** 2 != min_val:
	min_root += 1

sum_val = 0
for v in range(min_root, max_root+1):
	sum_val += v ** 2

if sum_val == 0:
	print(-1)
else:
	print(sum_val)
	print(min_root ** 2)
