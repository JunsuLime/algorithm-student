# Find a stair number
# 9
# ~
# 1   
#

n = int(input())

# index 0 ~ 9
stair_result = [1 for _ in range(10)]
# there is no number started from 0
stair_result[0] = 0

for _ in range(n-1):
	tmp_result = stair_result[:]
	# clean stair result
	for i in range(len(stair_result)):
		stair_result[i] = 0

	for i in range(len(stair_result)):
		if 0 <= i-1 < len(stair_result):
			stair_result[i] += tmp_result[i-1]
		if 0 <= i+1 < len(stair_result):
			stair_result[i] += tmp_result[i+1]

print(sum(stair_result) % 1000000000)

