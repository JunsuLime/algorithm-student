def work(s, command):
	command = command.split()

	if len(command) == 1:
		c = command[0]
		if c == "top":
			if not s:
				print(-1)
			else:
				print(s[len(s) - 1])
		elif c == "size":
			print(len(s))
		elif c == "empty":
			if not s:
				print(1)
			else:
				print(0)
		elif c == "pop":
			if not s:
				print(-1)
			else:
				print(s.pop())
	elif len(command) == 2:
		c = command[0]
		arg = int(command[1])
		s.append(arg)


n = int(input())
stack = list()

for i in range(n):
	work(stack, input())
