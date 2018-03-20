import math

def work(start, end):

	# 1 ~ n-1, n, n-1 ~ 1
	# sum: n ** 2
	# count: 2 * n - 1
	distance = end - start
	n = int(math.sqrt(distance))

	if n ** 2 == distance:
		return 2 * n - 1
	else:
		# how many maximum n needed to satisfy distance
		remain = distance - n ** 2
		if remain % n == 0:
			return 2 * n - 1 + int(remain / n)
		else:
			return 2 * n - 1 + int(remain / n + 1)


test_case = int(input())
for _ in range(test_case):
	start, end = map(int, input().split())
	print(work(start, end))
