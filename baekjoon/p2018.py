n = int(input())

# search that n can be represented by sum of n natural numbers.

i = 2
# number itself case is already counted
count = 1
while True:
	divide_val = int(n / i)
	if i % 2 == 0:
		# b_num is div count / 2 num
		# ex) [2,3,4,5,6] -> b_num = 2
		b_num = i / 2 - 1
		# if i is too large to make sum
		if divide_val - b_num <= 0:
			break
		# result of sum is not equal to n -> only i++
		elif (divide_val * 2 + 1) * (i >> 1) != n:
			i += 1
			continue
	else:
		b_num = int(i / 2)
		# if i is too large to make sum
		if divide_val - b_num <= 0:
			break
		# result of sum is not equal to n -> only i++
		elif divide_val * i != n:
			i += 1
			continue
	
	i += 1
	count += 1
print(count)
