n, k = map(int, input().split())
m = [[-1 for _ in range(0, k+1)] for _ in range(0, n+1)]

for i in range(0, k+1):
	m[0][i] = 0
for j in range(0, n+1):
	m[j][0] = 1


# print("-------------------")
for i in range(1, n+1):
	for j in range(1, k+1):
		# for l in m:
		# 	print(l)
		m[i][j] = m[i-1][j-1] + m[i-1][j]
		
		# print("-----------------------")

print(m[n][k] % 10007)		

