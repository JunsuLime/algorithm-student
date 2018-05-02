# problem 1 - find right parenthesis {}() right , (] false
def solve_p1(input_string):
	s = list()
	for c in input_string:
		if c == '(' or c == '[' or c == '{':
			s.append(c)
		elif len(s) == 0:
			return False
		else:
			top = s[len(s)-1]
			if c == ')' and top == '(':
				s.pop()
			elif c == '}' and top == '{':
				s.pop()
			elif c == ']' and top == '[':
				s.pop()
			else:
				return False

	if len(s) == 0:
		return True
	else:
		return False

# problem 2 - block 1, 2, 3, 4 heights are exist. find number of ways to build N height tower
def solve_p2(n):
	b_list = [1 for _ in range(4)]

	# start from 0, goto n
	for i in range(n-1):
		copied_p = b_list[:]
		b_list[0] = b_list[1] + copied_p[0]
		b_list[1] = b_list[2] + copied_p[1]
		b_list[2] = b_list[3] + copied_p[2]
		b_list[3] = copied_p[0]
	return b_list[0]


def solve_p3(s):
	from  collections import Counter

	tail = 0
	head = 0

	# stored max capacity is 2
	stored = Counter()
	max_length = 0

	for ch in s:
		# if character is already in stored set or stored item count < 2
		if ch in stored or len(stored.keys()) < 2:
			pass
		# if stored container is full, then increment tail until drop one time
		else:
			while len(stored.keys()) == 2:
				stored[s[tail]] -= 1
				if stored[s[tail]] == 0:
					stored.pop(s[tail])
				tail += 1
		
		head += 1
		# store ch on `stored`
		stored[ch] += 1
		# update max length
		max_length = max(max_length, head-tail)
		print(head, tail, ch, stored)

	return max_length

if __name__ == '__main__':
	print(solve_p3(input()))


