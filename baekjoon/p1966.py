from collections import deque

def work():
	docs_num, check = map(int, input().split())
	
	tracker = check
	q = deque(map(int, input().split()))

	print_order_counter = 0

	while len(q) != 0:
		front = q[0]

		is_printable = True
		# send it to back
		for item in q:
			if item > front:
				q.popleft()
				q.append(front)
				is_printable = False

				if tracker == 0:
					tracker = len(q) - 1
				else:
					tracker -= 1
				break

		# print
		if is_printable:
			q.popleft()
			print_order_counter += 1
			if tracker == 0:
				return print_order_counter
			else:
				tracker -= 1


		



case_num = int(input())

for _ in range(case_num):
	print(work())
