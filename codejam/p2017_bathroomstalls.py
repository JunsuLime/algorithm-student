def print_answer(idx, answer):
	print("Case #%d: %d %d" % (idx+1, answer[0], answer[1])

def work(s):
	"""
	l: distance between left nearest filled stall
	r: distance between right nearest filled stall

	go to empty stall where min(l, r) is max
	in tie case, go to leftmost emtpy stall

	return last person's min(l, r), max(l, r)
	@s: input string
	@return: min(l, r), max(l, r)
	"""
	
	b_num, p_num = map(int, s.split())
	
	
	

test_case = int(input())

for i in range(test_case):
	print_answer(i, work(input()))
