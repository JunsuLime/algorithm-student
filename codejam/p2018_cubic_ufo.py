import math


I_POINTS = [(0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5)]
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2


test_case = int(input())

def easy_use_mat(mat):
	ret_mat = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			ret_mat[j][i] = mat[i][j]
	return ret_mat

def test_distance(mat):
	mat = easy_use_mat(mat)
	for coord in mat:
		distance = math.sqrt(coord[0] ** 2 + coord[1] ** 2 + coord[2] ** 2)
		if 0.5 - 10e-6 <= distance <= 0.5 + 10e-6:
			pass
		else:
			print("coord: %r" % coord)
			print("failure distance")

def test_angle(mat):
	mat = easy_use_mat(mat)
	mat_len = len(mat)
	for i in range(mat_len):
		for j in range(i+1, mat_len):
			angle = math.acos((mat[i][0]*mat[j][0] + mat[i][1]*mat[j][1] + mat[i][2]*mat[j][2]) / (0.5) * (0.5))
			if math.pi / 2 - 10e-6 <= angle <= math.pi / 2 - 10e-6:
				pass
			else:
				print("lower bound %f" % (math.pi / 2 - 10e-6))
				print("upper bound %f" % (math.pi / 2 + 10e-6))
				print("failure angle: %r" % angle)


def print_output(i, coord):
	print("Case #%d:" % (i+1))
	print("%.16f %.16f %.16f" % (coord[0][0], coord[1][0], coord[2][0]))
	print("%.16f %.16f %.16f" % (coord[0][1], coord[1][1], coord[2][1]))
	print("%.16f %.16f %.16f" % (coord[0][2], coord[0][2], coord[2][2]))

	# test_distance(coord)
	# test_angle(coord)

def print_mat(mat):
	print("----------mat start---------")
	for row in mat:
		print(row)
	print("----------mat end---------")

def mat_mul(mat1, mat2):
	row1 = len(mat1)
	col1 = len(mat1[0])
	row2 = len(mat2)
	col2 = len(mat2[0])

	if col1 != row2:
		raise Exception

	result = [[0 for _ in range(col2)] for _ in range(row1)]
	for i in range(row1):
		for j in range(col2):
			for k in range(col1):
				result[i][j] += mat1[i][k] * mat2[k][j]
	
	return result

def rotate_mat_3d(axis, angle):
	r_mat = [[0, 0, 0] for _ in range(3)]
	if axis == X_AXIS:
		r_mat[0][0] = 1
		r_mat[1][1] = math.cos(angle)
		r_mat[2][2] = math.cos(angle)
		r_mat[1][2] = -math.sin(angle)
		r_mat[2][1] = math.sin(angle)
	elif axis == Y_AXIS:
		r_mat[0][0] = math.cos(angle)
		r_mat[1][1] = 1
		r_mat[2][2] = math.cos(angle)
		r_mat[0][2] = math.sin(angle)
		r_mat[2][0] = -math.sin(angle)
	elif axis == Z_AXIS:
		r_mat[0][0] = math.cos(angle)
		r_mat[1][1] = math.cos(angle)
		r_mat[1][0] = math.sin(angle)
		r_mat[0][1] = -math.sin(angle)
		r_mat[2][2] = 1

	return r_mat


def work():
	A = float(input())
	# print("A: %f" % A)

	def face_one():
		# print("face_one is called")
		return I_POINTS
	def face_two():
		# print("face_two is called")
		i_points = list(map(list, I_POINTS))

		# First, Find angle a
		# cos(a) + sin(a) == A, 1 + sin(2a) == A ** 2, a = math.asin(A ** 2 - 1) / 2
		a = math.asin(A ** 2 - 1) / 2
		return mat_mul(rotate_mat_3d(Z_AXIS, a), i_points)

	def face_three():
		# print("face_three is called")
		i_points = list(map(list, I_POINTS))

		# First, rotate cube -> max in face_two
		i_points = mat_mul(rotate_mat_3d(Z_AXIS, math.pi/4), i_points)

		# Second, Find angle b: (2 * cos(b) + sqrt(2) * cos(b)) * sqrt(2) / 2 = A
		# sqrt(6) * sin(x+b) = sqrt(2) * A
		# sin(x+b) = A / sqrt(3)
		# x + b = math.asin(A / sqrt(3)
		# b = math.asin(A / sqrt(3)) - x
		# b = math.asin(A / sqrt(3)) - math.acos(1 / sqrt(3))
		b = math.asin(A / math.sqrt(3)) - math.acos(1 / math.sqrt(3))
		return mat_mul(rotate_mat_3d(X_AXIS, b), i_points)

	if A <= 1:
		return face_one()
	elif 1 <= A <= math.sqrt(2):
		return face_two()
	else:
		return face_three()


	return [(0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5)]


for i in range(test_case):
	print_output(i, work())

