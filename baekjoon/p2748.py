# Bottom-Up

n = int(input())

p_list = [-1 for _ in range(n + 1)]


def p_function(n):
	if n == 0 or n == 1:
		return n
	elif p_list[n] != -1:
		return p_list[n]
	else:
		result = p_function(n - 1) + p_function(n - 2)
		p_list[n] = result
		return result

print(p_function(n))
