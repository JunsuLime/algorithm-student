def binary_search(l, e):
	"""
	l must be sorted list
	l: list of number
	e: key value we want to find

	return: index of e in l. if not exist, return -1
	"""
	low = 0
	high = len(l) - 1

	while low <= high:
		mid = low + int((high - low) / 2)
		# print(low, high, mid)
		if e > l[mid]:
			low = mid + 1
		elif e < l[mid]:
			high = mid - 1
		else:
			return mid
	
	return -1

def three_sum_search(l):
	"""
	l must be sorted list

	l: list of number (search pool)

	return count of three sum set
	"""

	count = 0

	for idx, i in enumerate(l):
		for j in l[idx + 1:]:
			zero_sum_val = - (i + j)
			zero_val_index = binary_search(l, zero_sum_val)

			if zero_val_index != -1:
				print(i, j, l[zero_val_index])
				count += 1

	return count

if __name__ == "__main__":
	a = [2, 4, 6, 7, -2, 0, -4, -1, -3, 1]
	a.sort()
	print(three_sum_search(a))

