# memoization

n = int(input())

p_list = list()

p_list.append(0)
p_list.append(1)

# except 0, 1 because it already computed
for i in range(2, n + 1):
	p_list.append(p_list[i-2] + p_list[i-1])

print(p_list[len(p_list) - 1])
