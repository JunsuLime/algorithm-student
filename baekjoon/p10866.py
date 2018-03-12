from collections import deque

def work(q, command):
	command = command.split()

	if len(command) == 2:
		arg = command[1]
		command = command[0]

		if command == "push_front":
			q.appendleft(arg)
		elif command == "push_back":
			q.append(arg)
	elif len(command) == 1:
		command = command[0]
		if command == "pop_front":
			if len(q) == 0:
				print(-1)
			else:
				print(q.popleft())
		elif command == "pop_back":
			if len(q) == 0:
				print(-1)
			else:
				print(q.pop())
		elif command == "size":
			print(len(q))
		elif command == "empty":
			if len(q) == 0:
				print(1)
			else:
				print(0)
		elif command == "front":
			if len(q) == 0:
				print(-1)
			else:
				print(q[0])
		elif command == "back":
			if len(q) == 0:
				print(-1)
			else:
				print(q[len(q) - 1])

n = int(input())

queue = deque()
for _ in range(n):
	work(queue, input())
