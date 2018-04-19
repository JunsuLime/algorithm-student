def binary_search(l, key):
	"""
	-Description-

	Search key value index with binary search.
	Assuming that l's sort order is ascending.
	
	This function's input is sorted_list and key value
	output is key value's index. If not exist, return -1.

	-Time Complexity-

	O(lg(len(l)))
	"""

	# half-open interval
	# left is closed and right is opened
	left = 0
	right = len(l)

	while left < right:
		mid = (left+right) // 2
		if key > l[mid]:
			left = mid + 1

		elif key < l[mid]:
			right = mid
		else:
			return mid
	
	return -1


if __name__ == '__main__':
	pass
