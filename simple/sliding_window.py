def sliding_window_average_list(l, window_size):
	"""
	-Description-

	With input(list, window_size)
	find sliding window average list

	1) find first sliding window partial_sum
	2) iterate ... another window partial_sum by 1)'s value
	3) keep going

	-Time Complexity-

	O(len(l))
	"""
	average_list = list()
	
	if len(l) <= window_size:
		average_list.append(sum(l))
		return average_list

	partial_sum = 0
	for i in range(window_size):
		partial_sum += l[i]
	
	average_list.append(partial_sum / window_size)
	for i in range(window_size, len(l)):
		partial_sum -= l[i-window_size]
		partial_sum += l[i]

		average_list.append(partial_sum / window_size)
	
	return average_list

def sliding_window_max_sum(l):
	pass

if __name__ == '__main__':
	pass
