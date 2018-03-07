n = int(input())

stack = list()
push_num = 1

results = list()

def push(s):
	global push_num, results
	s.append(push_num)
	push_num += 1
	results.append('+')

def pop(s):
	global results
	s.pop()
	results.append('-')

def work(s, number):
	if not s:
		top = 0
	else:
		top = s[len(s) - 1]

	if top > number:
		return False
	
	while top < number:
		push(s)	
		top = s[len(s) - 1]
	pop(s)
	return True

r = True
for i in range(n):
	r = work(stack, int(input()))
	if not r:
		break

if r:
	for rr in results:
		print(rr)
else:
	print("NO")
