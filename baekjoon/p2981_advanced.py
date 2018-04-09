import math


def print_output(results):
	results = str(results)
	results = results.replace('[', '')
	results = results.replace(']', '')
	results = results.replace(',', '')
	print(results)

def read_input():
	n = int(input())

	l = list()
	first_input = int(input())

	# all equation linked with first equation
	for i in range(n-1):
		l.append(abs(int(input())-first_input))
	l.sort()
	return l


def gcd(a, b):
	divided_val = max(a, b)
	divider = min(a, b)

	while True:
		remainder = divided_val % divider
		if remainder == 0:
			return divider

		divided_val = divider
		divider = remainder

def all_dividers(num):
	n = int(math.sqrt(num))

	dividers = set()

	# other common case
	for i in range(1, n+1):
		if num % i == 0:
			dividers.add(i)
			dividers.add(num // i)
	
	if 1 in dividers: 
		dividers.remove(1)

	dividers = list(dividers)
	dividers.sort()
	return dividers


s_list = read_input()

while True:
	merged_list = list()

	# s_list must be even length for easy calculation
	if len(s_list) % 2 != 0:
		merged_list.append(s_list[len(s_list)-1])

	for i in range(0, len(s_list)-1, 2):
		partial_gcd = gcd(s_list[i], s_list[i+1])
		merged_list.append(partial_gcd)
	s_list = merged_list
	
	if len(s_list) == 1:
		break
	

gcd_of_all = s_list[0]
d_list = all_dividers(gcd_of_all)
print_output(d_list)
