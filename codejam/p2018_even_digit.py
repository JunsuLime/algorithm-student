# Time Complexity: O(n)
# 

import sys

test_case = int(sys.stdin.readline())

def work():
	# number = list(sys.stdin.readline().rstrip())
	number = sys.stdin.readline().rstrip()

	value = 0
	for i in range(len(number)):
		digit = int(number[i])
		
		# odd number
		if digit % 2 != 0:
			# if has next digit
			if i != len(number)-1:
				# from current digit -> build number
				n = 0
				for j in range(i, len(number)):
					n += 10 ** (len(number)-j-1) * (int(number[j]))
					
				if digit == 9:
				 	# from current digit -> all 8
					comp1 = 0
					for j in range(i, len(number)):
						comp1 += 10 ** (len(number)-j-1) * 8
					value = n - comp1
				else:
					# compare 
					# 1. current -1 and next all -> 8
					# 2. current +1 and next all -> 0
					comp1 = 10 ** (len(number)-i-1) * (digit-1)
					for j in range(i+1, len(number)):
						comp1 += 10 ** (len(number)-j-1) * 8
					comp2 = 10 ** (len(number)-i-1) * (digit+1)

					value = min(n-comp1, comp2-n)
				break
			# if it is last index
			else:
				value = 1
	
	return value

for i in range(test_case):
	sys.stdout.write('Case #%d: %d\n' % (i+1, work()))
