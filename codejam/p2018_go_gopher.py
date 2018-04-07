import math
import logging

test_case = int(input())

LEFT_TOP = (500, 500)
MOVE = ((1, 0), (0, 1), (-1, 0), (0, -1))

def mul_pair(num):
	n = int(math.sqrt(num))
	while True:
		if num % n == 0:
			return n, num // n
		else:
			n += 1

class WorkEnd(Exception):
	pass

class Failure(Exception):
	pass

def work():
	"""
	go_gopher, random picker in 3*3 range.

	must fill all section so order of pick dont care.. OK
	but avoid to try pick place that already prepared.
	"""
	area = int(input())


	width, height = mul_pair(area)
	orchard = [[0 for _ in range(height)] for _ in range(width)]

	def try_pick(tx, ty):
		x = tx
		y = ty
		if tx < 1:	x = 1
		if ty < 1:	y = 1
		if tx > width-2: x = width-2
		if ty > height-2: y = height-2

		return pick_target(x, y, tx, ty)
	
	def pick_target(x, y, tx, ty):
		if orchard[tx][ty] == 1:
			return tx, ty
		else:
			return pick(x, y)

	def pick(x, y):
		print("%d %d" % (LEFT_TOP[0] + x, LEFT_TOP[1] + y), flush=True)
		x, y = map(int, input().split())
		if x == 0 and y == 0:
			raise WorkEnd
		if x == -1 and y == -1:
			raise Failure
		x -= LEFT_TOP[0]
		y -= LEFT_TOP[1]
		orchard[x][y] = 1
		return x, y
	

	def kill_them_all():
		all_prepared = True

		for i in range(width):
			for j in range(height):
				x, y = try_pick(i, j)
				all_prepared = all_prepared and (x == i and y == j)	

		return all_prepared
	

	while True:
		try:
			if kill_them_all():
				break
		except WorkEnd:
			break
		except Failure:
			break


for i in range(test_case):
	work()

