import math

test_case_num = int(input())
test_case_list = list()
for _ in range(test_case_num):
	test_case_list.append(int(input()))


max_filter_num = max(test_case_list)
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
# print(test_case_list)

for n in test_case_list:
	# print("case: %d" % n)
	start = n >> 1
	for i in range(start, 1, -1):
		j = n - i
		# print("[%d %d]" % (j, i))
		if p_filter[i] == 1 or p_filter[i] == -1:
			if p_filter[j] or p_filter[j] == -1:
				print("%d %d" % (i, j))
				break


