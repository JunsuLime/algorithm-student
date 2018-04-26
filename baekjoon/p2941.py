input_string = input()

# finite state machine

def other_solution(s):
	cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
	for c in cro:
		s = s.replace(c, 'C')
	return len(s)

count = 0
ref = 0

s_len = len(input_string)

while ref < len(input_string):
	cur = input_string[ref]
	if ref+1 < s_len and cur == 'c' and (input_string[ref+1] == '=' or input_string[ref+1] == '-'):
		ref += 2
	elif cur == 'd':
		if ref+1 < s_len and input_string[ref+1] == 'z':
			if ref+2 < len(input_string) and input_string[ref+2] == '=':
				ref += 3
			else:
				ref += 1
		elif ref+1 < s_len and input_string[ref+1] == '-':
			ref += 2
		else:
			ref += 1
	elif ref+1 < s_len and cur == 'l' and input_string[ref+1] == 'j':
		ref += 2
	elif ref+1 < s_len and cur == 'n' and input_string[ref+1] == 'j':
		ref += 2
	elif ref+1 < s_len and cur == 's' and input_string[ref+1] == '=':
		ref += 2
	elif ref+1 < s_len and cur == 'z' and input_string[ref+1] == '=':
		ref += 2
	else:
		ref += 1

	count += 1
print(count)

