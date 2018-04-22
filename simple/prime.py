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

if __name__ == '__main__':
	pass
