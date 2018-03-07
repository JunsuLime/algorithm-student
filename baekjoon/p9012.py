STATE_OPEN = 0
STATE_CLOSE = 1

def work(p_string):
		
	stack = list()

	state = STATE_OPEN
	ref = 0

	while ref < len(p_string):
		input_char = p_string[ref]

		if state == STATE_OPEN:
			if input_char == '(':
				ref += 1
				stack.append(input_char)
			else:
				state = STATE_CLOSE
		elif state == STATE_CLOSE:
			if input_char == '(':
				state = STATE_OPEN
			else:
				if not stack:
					# if stack is empty
					return False
				else:
					ref += 1
					stack.pop()
	
	return len(stack) == 0


n = int(input())
for i in range(n):
	r = work(input())
	if r:
		print("YES")
	else:
		print("NO")

