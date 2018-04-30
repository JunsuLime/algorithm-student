# Time Complexity: < O(8 ^ (empty / 3))  may be..
# Elapsed time: 68ms
#
# Complete search problem
# Little bit different with books solution.
# In my case, check 8 block state -> must fill the blank

import sys

test_case = int(sys.stdin.readline())
blocks = (
			# (0, 0) is abbreviated because of assumption that all block have (0, 0) point
			((0, 1), (-1, 1)),
			#  0
			# s0
			((1, 0), (1, 1)),
			# s
			# 00
			((0, -1), (1, -1)),
			# 0s
			# 0
			((-1, -1), (-1, 0)),
			# 00
			#  s
			((1, 0), (0, 1)),
			# s0
			# 0
			((0, -1), (1, 0)),
			# 0s
			#  0
			((-1, 0), (0, -1)),
			#  0
			# 0s
			((-1, 0), (0, 1)),
			# 0
			# s0
			((0, 1), (1, 1)),
			# s0
			#  0
			((1, -1), (1, 0)),
			#  s
			# 00
			((0, -1), (-1, -1)),
			# 0
			# 0s
			((-1, 0), (-1, 1)),
			# 00
			# s
		 )

EMPTY = '.'
WALL = '#'

def print_cover(c):
	"""
	Debugging ...
	"""
	print('---------------')
	for line in c:
		print(line)
	print('---------------')


def work():
	# read width and height values
	width, height = map(int, sys.stdin.readline().split())
	board = list()

	empty_count = 0
	for _ in range(width):
		# rstrip remove return carage
		# save map on board list
		line = list(sys.stdin.readline().rstrip())
		board.append(line)

		empty_count += line.count(EMPTY)
	
	# if empty cell count cannot be divided by 3
	# there are no case that appropreatily fill it.
	if empty_count % 3 != 0:
		return 0

	def search(c, x, y, e_count):
		"""
		@param c: current cover state
		@param x: in current state - ref x
		@param y: in current state - ref y
		@param e_count: remained empty_count value

		@return: at this state (c), return available case count.
		"""
		if not (0 <= x < width and 0 <= y < height):
			return 0

		case_count = 0
		for b in blocks:
			# if candidate position are WALL or OutOfIndex, then ignore it.
			if not ((0 <= x+b[0][0] < width) and (0 <= x+b[1][0] < width)):
				continue
			if not ((0 <= y+b[0][1] < height) and (0 <= y+b[1][1] < height)):
				continue
			if c[x+b[0][0]][y+b[0][1]] == WALL:
				continue
			if c[x+b[1][0]][y+b[1][1]] == WALL:
				continue
			
			# wow find it
			if e_count == 3:
				case_count += 1
				continue

			# cover it
			c[x][y] = WALL
			c[x+b[0][0]][y+b[0][1]] = WALL
			c[x+b[1][0]][y+b[1][1]] = WALL

			# get next x, y to ref
			nx = x
			ny = y+1
			while nx < width:
				success = False
				while ny < height:
					if c[nx][ny] != WALL:
						success = True
						break
					ny += 1
				if success:
					break
				nx += 1
				ny = 0

			# recurviely search again
			case_count += search(c, nx, ny, e_count-3)
			
			# recover origin state
			c[x][y] = EMPTY
			c[x+b[0][0]][y+b[0][1]] = EMPTY
			c[x+b[1][0]][y+b[1][1]] = EMPTY

		return case_count
	
	# find first empty cell
	for i, line in enumerate(board):
		for j, char in enumerate(line):
			if char == EMPTY:
				return search(board, i, j, empty_count)
	return 0

for _ in range(test_case):
	print(work())
