import sys
import math


test_case = int(sys.stdin.readline())

def geometric_seq_sum(a, r, n):
	return (a*(1 - math.pow(r, n))) / (1 - r)

def work():
	n, redip = map(int, sys.stdin.readline().rstrip().split())
	dip = redip + 1

	num_list = list(map(int, sys.stdin.readline().rstrip().split()))
	num_list.sort(reverse=True)	# O(nlogn)

	expected_value = 0

	v = 0

	# pick max value
	idx = 0
	cur = num_list[0]	
	cur_count = 0
	while True:
		if idx == n:
			return cur	
		if cur > num_list[idx]:
			prob = cur_count / n
			pick_other_prob = (n-idx) / n	
			g_sum = geometric_seq_sum(prob, pick_other_prob, dip)
			v += g_sum
			expected_value += cur * g_sum
			# print(expected_value)
			break
		else:
			cur_count += 1
			idx += 1

	cur = num_list[idx]
	cur_count = 0
	for i in range(idx, n+1):
		if i == n:
			p1 = math.pow((cur_count / n), dip)
			v += p1
			# print(cur, cur_count, n, dip)
			expected_value += cur * p1
			# print(expected_value)
		elif cur > num_list[i]:
			p1 = math.pow(((n-(i-cur_count)) / n), dip)
			p2 = math.pow(((n-i) / n), dip)
			# print(cur, n-(i-cur_count), n, n-i, n, dip)
			expected_value += cur * (p1 - p2)
			
			# print(expected_value)
			v += p1-p2
			cur = num_list[i]
			cur_count = 1
		else:
			cur_count += 1
	
	# print(v)
	return expected_value

for i in range(test_case):
	sys.stdout.write('Case #%d: %.9f\n' % (i+1, work()))
