import sys

test_case = int(input())

def max_rect(fence, left, right):
	"""
	get max rect between left, right [) range

	if divide this by left side and right side
	case 1: max rect is only appear in one side
	case 2: max rect is appear along left side and right side
	"""
	if right - left == 1:
		return fence[left]
		# mid = int((left+right) / 2)
	mid = (left+right) >> 1
	
	# Case 1: max_rect is in only left part or only right part
	m_rect = max(max_rect(fence, left, mid), max_rect(fence, mid, right))
		# Case 2: max_rect is in left and right both
	ref_left = mid
	ref_right = mid
	height = min(fence[ref_left], fence[ref_right])
	
	while True:
		m_rect = max(m_rect, (ref_right - ref_left+ 1) * height)
		
		# if left and right both can be expanded
		if left <= ref_left-1 and ref_right+1 < right:
			# if next left fence is taller than right next fence,
			# choose left fence
			if fence[ref_left-1] > fence[ref_right+1]:
				ref_left -= 1
				height = min(fence[ref_left], height)
		 	# else, choose right fence
			else:
				ref_right += 1
				height = min(fence[ref_right], height)
		
		# if only left can be expanded
		elif left <= ref_left-1:
			ref_left -= 1
			height = min(fence[ref_left], height)
		
		# if only right can be expanded
		elif ref_right+1 < right:
			ref_right += 1
			height = min(fence[ref_right], height)
		
		# no more expand .. break
		else:
			break

	return m_rect

def work():
	n = int(input())
	fence = list(map(int, sys.stdin.readline().rstrip().split()))

	return max_rect(fence, 0, len(fence))

for _ in range(test_case):
	sys.stdout.write('%d\n' % work())
