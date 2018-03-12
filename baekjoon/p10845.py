from collections import deque

def work(q, command):
	command = command.split()
	if len(command) == 1:
		command = command[0]
		if command == "pop":
			if len(q) == 0:
				print(-1)
			else:
				print(q.popleft())
			# if empty -> print -1
			pass
		elif command == "size":
			print(len(q))
			pass
		elif command == "empty":
			if len(q) == 0:
				print(1)
			else:
				print(0)
			# if empty -> 1, not -> 0
			pass
		elif command == "front":
			if len(q) == 0:
				print(-1)
			else:
				print(q[0])
			# if empty -> -1, not -> front
			pass
		elif command == "back":
			if len(q) == 0:
				print(-1)
			else:
				print(q[len(q) - 1])
			# if empty -> -1, not -> back
			pass
	elif len(command) == 2:
		arg = command[1]
		command = command[0]

		if command == "push":
			q.append(arg)

queue = deque()

n = int(input())

for _ in range(n):
	work(queue, input()) 
