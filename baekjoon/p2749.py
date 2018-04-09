import math

# solve fibonnaci problem with matrix

f_matrix = ((0, 1), (1, 1))
e_matrix_cache = dict()	# key: exp, value: exp_matrix

def mat_mul(mat1, mat2):
	if len(mat1) != len(mat2[0]):
		raise Exception
	
	matrix = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
	for i in range(len(mat1)):
		for j in range(len(mat2[0])):
			for k in range(len(mat2)):
				matrix[i][j] += mat1[i][k] * mat2[k][j]
				matrix[i][j] %= 1000000

	return matrix

n = int(input())
exp = int(math.log2(n))

e_matrix_cache[0] = f_matrix
cur_matrix = f_matrix
for e in range(1, exp+1):
	cur_matrix = mat_mul(cur_matrix, cur_matrix)
	e_matrix_cache[e] = cur_matrix


cur_matrix = ((1, 0), (0, 1))
cur = n
while cur > 0:
	exp = int(math.log2(cur))
	cur = cur - 2 ** exp

	cur_matrix = mat_mul(cur_matrix, e_matrix_cache[exp])

print(cur_matrix[0][1])
