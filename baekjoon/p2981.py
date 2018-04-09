import math
import itertools
import sys

n = int(input())

l = list()
l.append(int(input()))

for i in range(n-1):
	e = int(input())
	l[i] = abs(l[i] - e)
	if i != n-2:
		l.append(e)

l.sort()
# print(l)

def gcd(a, b):
	divided_val = a
	divider = b 

	while True:
		remainder = divided_val % divider
		if remainder == 0:
			return divider
		divided_val = divider
		divider = remainder

def extract_prime_factors(num):
	PRIME = 1
	NOT_PRIME = 0

	# except 0 and 1, include index n
	e_filter = [PRIME for _ in range(num+1)]
	e_filter[0] = NOT_PRIME
	e_filter[1] = NOT_PRIME

	for checker in range(2, num+1):
		if e_filter[checker] == NOT_PRIME:
			continue

		mul = 1
		while True:
			mul += 1
			cur = checker * mul
			
			if cur > num:
				break
			e_filter[cur] = NOT_PRIME
	# print(num)
	# print(e_filter)
	prime_factors = list()
	for idx, val in enumerate(e_filter):
		if val == PRIME and num % idx == 0:
			c = num // idx
			prime_factors.append(idx)

			while c % idx == 0:
				prime_factors.append(idx)
				c = c // idx
	
	return prime_factors

def get_all_divider(p):
	d_set = set()
	for i in range(1, len(p)+1):
		for c in itertools.combinations(p, i):
			divider = 1
			for e in c:
				divider *= e
			d_set.add(divider)
	return d_set

divide = gcd(l[1], l[0])
p_factors = extract_prime_factors(divide)
dividers = get_all_divider(p_factors)


results = list()
for d in dividers:
	all_success = True
	for e in l:
		if e % d != 0:
			all_success = False

	if all_success:
		results.append(d)
results.sort()

results = str(results)
results = results.replace('[', '')
results = results.replace(']', '')
results = results.replace(',', '')
print(results)
