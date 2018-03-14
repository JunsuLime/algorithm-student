n, k = map(int, input().split())

cache =[[-1 for _ in range(n + 1)] for _ in range(n + 1)]

def binomial_coefficient(n, k):
	if k == 0 or n == k:
		return 1
	elif k == 1 or n == k + 1:
		return n
	elif cache[n][k] != -1:
		return cache[n][k]
	else:
		result = binomial_coefficient(n - 1, k -1) + binomial_coefficient(n - 1, k)
		cache[n][k] = result

		return result

print(binomial_coefficient(n, k))
	
