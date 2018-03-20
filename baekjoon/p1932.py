candidate_list = list()

height = int(input())
first_floor = int(input())

candidate_list.append(first_floor)

for h in range(2, height + 1):
	current = list(map(int, input().split()))
	prev = candidate_list[:]
	candidate_list[0] += current[0]

	for i in range(1, len(candidate_list)):
		candidate_list[i] = current[i] + max(prev[i], prev[i-1])
	
	candidate_list.append(prev[h-2] + current[h-1])
print(max(candidate_list))
