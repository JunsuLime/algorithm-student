# To store large data, Use QuadTree
# Using for represent compressed black and white picture

import sys

def parse_tree(t_str, idx):
	if t_str[idx] == 'b' or t_str[idx] == 'w':
		return t_str[idx], idx+1
	else:
		# case of 'x'
		sub_tree = [None for _ in range(4)]
		idx += 1
		for i in range(4):
			sub_tree[i], idx = parse_tree(t_str, idx)
		
		return sub_tree, idx

# Solution 1
def work():
	tree_str = sys.stdin.readline().rstrip()
	tree, _ = parse_tree(tree_str, 0)
	
	def swap(t):
		if type(t) is not list:
			return

		for b in t:
			if type(b) is list:
				swap(b)

		# swap(0, 2), swap(1, 3)
		tmp = t[0]
		t[0] = t[2]
		t[2] = tmp
		tmp = t[1]
		t[1] = t[3]
		t[3] = tmp
	
	swap(tree)

	def compress_tree(t):
		if type(t) is not list:
			return t
		
		compressed = 'x'
		for b in t:
			compressed += compress_tree(b)

		return compressed
	
	return compress_tree(tree)


# Solution 2
def work_well():
	tree_str = list(sys.stdin.readline().rstrip())
	
	def reverse(start):
		if tree_str[start] == 'b' or tree_str[start] == 'w':
			return tree_str[start], start+1
		else:
			start += 1
			up_left, start = reverse(start)
			up_right, start = reverse(start)
			lower_left, start = reverse(start)
			lower_right, start = reverse(start)

			return 'x' + lower_left + lower_right + up_left + up_right, start

	# range of start, end [)
	return reverse(0)[0]

test_case = int(sys.stdin.readline())

for _ in range(test_case):
	print(work_well())
