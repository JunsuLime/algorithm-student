n = int(input())
num_list = list(map(int, input().split()))

# it can be solve by dynamic problem solving
# contigiousness is valid for all continuous val
# So, one of two
# 1) choose ref one only
# 2) choose current value
# choose max value one of two

max_current = num_list[0]
max_global = num_list[0]

for i in range(1, len(num_list)):
	max_current = max(num_list[i], max_current+num_list[i])
	if max_current > max_global:
		max_global = max_current

print(max_global)

