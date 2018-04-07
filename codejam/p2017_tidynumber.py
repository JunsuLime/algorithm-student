# when written in base 10 with no leading zeroes, have thier digits sorted in non-decreasing order.

import math

def hash(

def work(m_num):
	# In base 10, find m_num's digit num
	# Let's use combination with repetition
	result = 0

	digit_num = int(math.log10(m_num)) + 1

	# 1) find on max digit case 

	# 2) find on other cases
	for d_num in range(digit_num-1, 0, -1):
		# TODO: calculate 10 H d_num
		# n H k = n+k-1 C k
		result += 0

	print(m_num, digit_num)
	
	return m_num


def print_answer(idx, answer):
	print("Case #%d: %d\n" % (idx + 1, answer))



test_case = int(input())

for i in range(test_case):
	print_answer(i, work(int(input())))

