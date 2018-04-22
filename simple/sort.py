import random
import math
import heapq


def swap(l, idx1, idx2):
	tmp = l[idx1]
	l[idx1] = l[idx2]
	l[idx2] = tmp


class HeapTree(object):
	"""
	Min Heap Tree
	Min value is on the top of tree.
	"""

	class HeapEmpty(Exception):
		"""
		Exception is raised, In case that heap is empty but do pop
		"""
		pass

	EMPTY = None
	ROOT_IDX = 1

	def __init__(self):
		"""
		HeapTree's internal container is array list
		and it have its own length var.

		HeapTree's 0-index is not used, so EMPTY is assigned in there
		"""
		self.__container = list()
		self.__len = 0

		# root node is not used
		self.__container.append(HeapTree.EMPTY)

	def __iter__(self):
		for i in range(1, self.__len+1):
			yield self.__container[i]

	def add(self, e):
		"""
		HeapTree add function

		Added element is started from bottom of tree.
		They look up parent node and go up as high as possible.

		-Time Complexity-
		
		average: O(1)
		worst: O(log2(N))

		because half of heap's elements are in leaf node. So insertion
		average time complexity is O(1)
		"""
		# if empty spaces are not surfficient, create new empty space
		self.__len += 1
		if len(self.__container) < self.__len+1:
			extend_len = int(math.log2(self.__len+1))
			self.__container.extend([HeapTree.EMPTY]*extend_len)

		# first, set value on current empty space
		cur = self.__len
		self.__container[cur] = e

		while cur != HeapTree.ROOT_IDX:
			p_key, p_val = self.parent(cur)
			if p_val > self.__container[cur]:
				swap(self.__container, p_key, cur)
				cur = p_key
			else:
				break

	def parent(self, idx):
		"""
		get parent nodes key and value
		"""
		return idx >> 1, self.__container[idx >> 1]

	def children(self, idx):
		"""
		get children nodes key and value
		"""
		if 2*idx+1 > len(self.__container)-1:
			return ((2*idx, HeapTree.EMPTY), (2*idx+1, HeapTree.EMPTY))
		
		return ((2*idx, self.__container[2*idx]), (2*idx+1, self.__container[2*idx+1]))
	
	def __swap(self, idx1, idx2):
		swap(self.__container, idx1, idx2)
	
	
	def empty(self):
		"""
		check node is empty
		"""
		return self.__len == 0

	def contain(self, e):
		"""
		In HeapTree, contain function needs to do full scan.

		-Time Complexity-

		O(N)
		"""
		for i in range(1, self.__len+1):
			if self.__container[i] == e:
				return True
		return False

	def pop(self):
		"""
		Pop root node elements and reset heap data structure

		-Time Complexity-

		O(log2(N))
		"""
		if self.__len == 0:
			raise HeapTree.HeapEmpty
	
		ret_val = self.__container[HeapTree.ROOT_IDX]
		
		self.__swap(HeapTree.ROOT_IDX, self.__len)
		self.__container[self.__len] = HeapTree.EMPTY
	
		self.__len -= 1

		cur = HeapTree.ROOT_IDX
		while cur < self.__len:
			children_nodes = self.children(cur)

			min_child_idx = cur
			min_child_val = self.__container[cur]

			for child in children_nodes:
				# in 0 index, key is saved and 1 index, value is saved
				if child[0] < self.__len and min_child_val > child[1]:	
					min_child_idx = child[0]
					min_child_val = child[1]

			if min_child_idx == cur:
				break

			self.__swap(cur, min_child_idx)
			cur = min_child_idx
						
		return ret_val


def selection_sort(l):
	"""
	-Description-

	select min value and swap it.

	-Time Complexity-
	
	O(N**2)
	"""
	for i in range(len(l)):
		min_idx = i
		for j in range(i+1, len(l)):
			if l[j] < l[min_idx]:
				min_idx = j
		swap(l, min_idx, i)


def insertion_sort(l):
	"""
	-Description-

	During iteration, find item's appropriate location and swap

	-Time Complexity-

	O(N**2)
	"""
	for i in range(len(l)):
		for j in range(i, 0, -1):
			if l[j-1] > l[j]:
				swap(l, j-1, j)
			else:
				break


def merge_sort(l, sort=None):
	"""
	-Description-

	Divide and conquere approach. extra memory allocation is needed

	-Time Complexity-

	O(N*log2(N))
	"""

	def __merge_sort_internal(left, right):
		if left+1 >= right:
			return

		mid = (left + right) // 2
		__merge_sort_internal(left, mid)
		__merge_sort_internal(mid, right)

		j = mid
		left_copied = l[left:mid]
		right_copied = l[mid:right]

		left_cur = 0
		right_cur = 0
		for i in range(left, right):
			if left_cur == len(left_copied):
				l[i] = right_copied[right_cur]
				right_cur += 1
			elif right_cur == len(right_copied):
				l[i] = left_copied[left_cur]
				left_cur += 1
			elif left_copied[left_cur] <= right_copied[right_cur]:
				l[i] = left_copied[left_cur]
				left_cur += 1
			else:
				l[i] = right_copied[right_cur]
				right_cur += 1
	__merge_sort_internal(0, len(l))


def heap_sort(l):
	"""
	-Description-

	-Time Complexity-

	O(N*log2(N))
	"""
	heap = HeapTree()
	for e in l:
		heap.add(e)

	cur = 0
	while not heap.empty():
		l[cur] = heap.pop()
		cur += 1


def simple_heap_sort(l):
	"""
	-Description-

	-Time Complexity-
	"""
	h = l[:]
	heapq.heapify(h)

	cur = 0
	while len(h) != 0:
		l[cur] = heapq.heappop(h)
		cur += 1	
	

def quick_sort(l):
	"""
	-Descrption-

	Pick pivot and sort left and right partion
	divided by pivot

	-Time Complexity-

	O(log(N))
	"""
	def __partition(left, right):
		pivot = l[left]
		l_idx = left+1
		r_idx = right-1

		while l_idx <= r_idx:
			if pivot < l[r_idx]:
				r_idx -= 1
			elif l[l_idx] < pivot:
				l_idx += 1
			else:
				swap(l, l_idx, r_idx)
		
		swap(l, r_idx, left)
		return r_idx
		
	def __quick_sort_internal(left, right):
		if left < right:
			pivot = __partition(left, right)
			__quick_sort_internal(left, pivot)
			__quick_sort_internal(pivot+1, right)
			
	__quick_sort_internal(0, len(l))


def binary_search(l, key):
	"""
	-Description-

	Search key value index with binary search.
	Assuming that l's sort order is ascending.
	
	This function's input is sorted_list and key value
	output is key value's index. If not exist, return -1.

	-Time Complexity-

	O(log2(N))
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


def is_sorted(l):
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			return False
	return True


def shuffle(l):
	for i in range(len(l)):
		r = random.randrange(i, len(l))
		swap(l, r, i)


def sample_list(n):
	l = list(range(n))
	shuffle(l)
	return l


def test_sort(sort, n=10):
	l = sample_list(n)
	print('before: %r' % l)
	sort(l)
	print('after: %r' % l)


if __name__ == '__main__':
	test_sort(simple_heap_sort, n=10)
	l = list()

	heapq.heappush(l, (1,2))
	heapq.heappush(l, (2,5))

	heapq.heappush(l, (0, 100))

	print(heapq.heappop(l))
