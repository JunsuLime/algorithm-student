# only 1 digit number big and small
# so big % small => only 1 digit number too.

input_digits = list(map(int, input().split()))

big_digit = max(input_digits)
small_digit = min(input_digits)

while True:
	remained_digit = big_digit % small_digit
	if remained_digit == 0:
		break
	
	big_digit = small_digit
	small_digit = remained_digit

print('1'*small_digit)
