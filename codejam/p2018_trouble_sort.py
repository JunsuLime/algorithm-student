test_case = int(input())

MAX_VAL = 10 ** 9 + 1


def print_output(i, result):
	if type(result) is str:
		print("Case #%d: %s" % (i+1, result))
	else:
		print("Case #%d: %d" % (i+1, result))

def work():
	odd_list = list()
	even_list = list()

	input()
	for idx, e in enumerate(map(int, input().split())):
		if idx % 2 == 0:
			even_list.append(e)
		else:
			odd_list.append(e)

	
	# python sort is merge sort + insertion sort
	# so, big O - near log2n
	even_list.sort()
	odd_list.sort()

	if len(even_list) != len(odd_list):
		odd_list.append(MAX_VAL)

	prev_ev = -1
	prev_ov = -1

	# print(even_list)
	# print(odd_list)

	# just iteration -> big O: n
	for idx, val in enumerate(zip(even_list, odd_list)):
		ev, ov = val

		# print("prev_ev: %d, prev_ov: %d, ev: %d, ov: %d" % (prev_ev, prev_ov, ev, ov))
		if prev_ov > ev:
			return 2 * idx - 1
		elif ev > ov:
			return 2 * idx

		prev_ev, prev_ov = val
	
	return "OK"


for i in range(test_case):
	print_output(i, work())

