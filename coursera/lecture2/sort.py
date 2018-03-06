def __swap(l, idx1, idx2):
	tmp = l[idx1]
	l[idx1] = l[idx2]
	l[idx2] = tmp

def selection_sort(l):
	"""
	Data movement is minimal
	"""
	for i in range(len(l)):
		min_idx = i

		# select minimun value in remained array
		for j in range(i + 1, len(l)):
			if l[min_idx] > l[j]:
				min_idx = j
		__swap(l, i, min_idx)


def insertion_sort(l):
	"""
	If already sorted l, this is very good case.
	l is reversed sorted, worst case.

	good at partially sorted array
	"""
	for i in range(len(l) - 1):
		for j in range(i + 1, 0, -1):
			if l[j] < l[j - 1]:
				__swap(l, j, j - 1)
			else:
				break

def shell_sort(l):
	"""
	move entries more than one position at a time by h-sorting the array
	
	h-sorting: insertion sort, with stide length h.

	TODO: complete this code ... T_T
	"""
	def __updated_h(h):
		h = int(h / 3)
		
	def __max_h(h):
		while h < int(len(l) / 3):
			h = 3 * h + 1
		return h

	h = __max_h()
	
	while h >= 1:

		# h-sort the array
		for i in range(h, len(l)):
			for j in range(i, h, -h):
				if l[j] < l[j - h]:
					__swap(l, j, j-h)
				else:
					break

		h = __updated_h(h)
	

def shuffle(l):
	"""
	rearrange the array!
	"""
	import random
	for i in range(len(l)):
		r = random.randrange(i, len(l))
		__swap(l, r, i)

def convex_hull(l):
	"""
	Samllest convex set containing all the points

	return sequence of vertice in counterclockwise order
	
	Graham scan demo
	1) Coose point p with smallest y-coordinate.
	2) Sort points by polar angle with p
	3) Consider points in order; discard unless it create a ccw turn

	TODO: ,,,
	"""
	pass


def is_sorted(l):
	"""
	Test that the array is sorted
	
	return is_sorted
	"""
	for i in range(len(l) - 1):
		if l[i] > l[i + 1]:
			return False
	
	return True


