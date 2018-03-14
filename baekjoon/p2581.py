import math

min_num = int(input())
max_num = int(input())

max_filter_num = max_num
max_checker = int(math.sqrt(max_filter_num)) + 1

# print(max_filter_num, max_checker)

if max_filter_num < 2:
	max_filter_num = 2

p_filter = [-1 for _ in range(max_filter_num + 1)]

p_filter[0] = 0
p_filter[1] = 0
# 2 is prime number
p_filter[2] = 1

for i in range(2, max_checker + 1):
	# print("checker: %r" % i)
	if p_filter[i] == -1:
		p_filter[i] = 1
	elif p_filter[i] == 0:
		continue
	
	count = i
	while count < len(p_filter):
		if p_filter[count] == -1:
			p_filter[count] = 0
		count += i

# print(p_filter)


s = 0
min_val = -1

for i in range(min_num, max_num + 1):
	if p_filter[i] == 1 or p_filter[i] == -1:
		if min_val == -1:
			min_val = i
		s += i

if min_val == -1:
	print(-1)
	exit()
print(s)
print(min_val)


