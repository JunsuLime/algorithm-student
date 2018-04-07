def output(i, result):
	if type(result) is int:
		result = str(result)
	print("Case #%d: %s" % (i+1, result))


def work(pancakes, flip_count):
	pancakes = list(pancakes)
	ff = 0

	for i in range(len(pancakes) - flip_count + 1):
		#print("flip %d" % i)
		p = pancakes[i]
		if p == '-':
			for j in range(flip_count):
				pf = pancakes[i+j]
				if pf == '-':
					pancakes[i+j] = '+'
				else:
					pancakes[i+j] = '-'
			#print(pancakes)
			ff += 1
	
	if '-' in pancakes:
		return "IMPOSSIBLE"
	else:
		return ff


test_case = int(input())

for i in range(test_case):
	pp, f_count = input().split()
	f_count = int(f_count)
	output(i, work(pp, f_count))

