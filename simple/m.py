import math

def is_prime(num):
	"""
	-Description-

	num can be represented
	num = a * b
	and min(a, b) <= sqrt(num)

	sieving with 2 ~ sqrt(num), num is alived
	then num is prime number

	this function's input is number 
	and output is number is prime ? T : F

	-Time Complexity-

	pass
	
	"""
	# TODO: How to calculate time complexity of eratosthenes sieve. check it

	# list contains 0 ~ num
	# 0 is prime and 1 is not prime
	sieve = [0 for _ in range(num+1)]
	
	n = int(math.sqrt(num))
	sieve[0] = 1
	sieve[1] = 1

	# sieving with 2 ~ sqrt(num)
	for i in range(2, n+1):
		# if n is not prime, we don't have to test it. 
		if sieve[i] == 1:
			continue

		# i is prime and numbers smaller than i
		# are already proved
		cur_index = i ** 2
		while cur_index < num + 1:
			sieve[cur_index] = 1
			cur_index += i
	
	return sieve[num] == 0

def karatsuba_fast_multiply(a, b):
	"""
	get result a*b

	if digit of a is 256 and digit of b is 256, then ...
	a = a1 * 10^256 + a0
	b = b1 * 10^256 + b0

	a*b = a1*b1*10^256 + (a1*b0 + a0*b1)*10^128 + a0*b0
	lets
	z0 = a0*b0
	z2 = a1*b1
	
	z1 = a1*b0 + a0*b1 = (a0+a1)*(b0+b1) - z0 - z2

	so only 3 multiply !
	"""
	def normalize(seq, base=10):
		seq.append(0)

		for i in range(len(seq)):
			if seq[i] < 0:
				borrow = (abs(seq[i]) + base-1) // base
				seq[i+1] -= borrow
				seq[i] += borrow * base
			else:
				seq[i+1] += seq[i] // base
				seq[i] %= base
		
		while len(seq) > 0 and seq[len(seq)-1] == 0:
			seq.pop()

	def multiply(seq1, seq2):
		result = [0 for _ in range(len(seq1)+len(seq2)+1)]
		for i in range(len(seq1)):
			for j in range(len(seq2)):
				result[i+j] += seq1[i] * seq2[j]

		normalize(result)
		return result

	def add_to(seq1, seq2, k):
		pass
	
	def sub_from(seq1, seq2):
		pass
	
	# if num1 is shorter than num2 -> swap it
	# num1 must bigger digit than num2
	if len(a) < len(b):
		return karatsuba_fast_multiply(b, a)
	if len(a) == 0 or len(b) == 0:
		return []
	
	half = len(a) >> 1
	a0 = a[:half]
	a1 = a[half:]
	b0 = b[:min(len(b), half)]
	b1 = b[min(len(b), half):]

	z2 = karatsuba_fast_multiply(a1, b1)
	z0 = karatsuba_fast_multiply(a0, b0)

	add_to(a0, a1, 0)
	add_to(b0, b1, 0)

	z1 = karatsuba_fast_multiply(a0, b0)
	sub_from(z1, z0)
	sub_from(z1, z2)

	ret = list()
	add_to(ret, z0, 0)
	add_to(ret, z1, half)
	add_to(ret, z2, half+half)
	return ret


if __name__ == '__main__':
	pass
