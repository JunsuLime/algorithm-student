from collections import deque

def work():
	commands = input()
	_ = input()

	array = input()
	array = array.replace('[', '').replace(']', '')
	
	if array == "":
		array = list()
	else:
		array = map(int, array.split(','))

	q = deque(list(array))

	r_flag = False
	for c in commands:
		if c == 'R':
			r_flag = not r_flag
		elif c == 'D':
			if len(q) == 0:
				print("error")
				return
			else:
				if r_flag:
					q.pop()
				else:
					q.popleft()
		else:
			print("error")
			return
	
	if r_flag:
		q.reverse()
	
	q = str(list(q))
	q = q.replace(' ', '')
	print(q)


test_case = int(input())

for _ in range(test_case):
	work()
