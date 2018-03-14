import math

n_list = list()
while True:
	n = int(input())
	if n == 0:
		break
	else:
		n_list.append(n)

max_filter_num = max(n_list) * 2
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


for n in n_list:
	counter = 0
	for i in range(n + 1, 2 * n + 1):
		if p_filter[i] == 1 or p_filter[i] == -1:
			counter += 1
	
	print(counter)

