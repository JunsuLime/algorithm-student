test_case = int(input())

def print_output(i, output):
	print('Case #%d: %d' % (i+1, output))

def work():
	"""
	def loop:
		x = extra_val

		(term+x) // week = line
		x = (term+x) % week
	"""
	month, term, week = map(int, input().split())
	x = 0
	line = 0

	# Phase 1: find circular loop
	remained_month = month
	while remained_month > 0:
		line += (term + x) // week
		x = (term + x) % week

		# ex)  week 4 and . . 1 2
		# then, x = 2

		remained_month -= 1
		if x != 0:
			# if x != 0 -> next month goes to next line so +1
			line += 1
		else:
			# find circular case because x is start from 0
			break
	
	# short case
	if remained_month == 0:
		return line

	# Phase 2: When we find circular rule on calendar line
	# per month_circle -> line is added on line_sum
	month_circle = month - remained_month
	line_sum = (month // month_circle) * line

	# After circular addition, add extra month
	remained_month = month % month_circle
	while remained_month > 0:
		line_sum += (term + x) // week
		x = (term + x) % week
		
		remained_month -= 1
		if x != 0:
			line_sum += 1

	return line_sum
	

for i in range(test_case):
	print_output(i, work())

