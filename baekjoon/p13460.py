from collections import deque

INVALID_POS = [0, 0]

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

WALL = '#'
HOLE = 'O'
EMPTY = '.'

width, height = map(int, input().split())

g_map = list()
init_r_pos = None
init_b_pos = None
for x in range(width):
	line = input()
	if 'R' in line:
		init_r_pos = [x, line.index('R')]
		line = line.replace('R', EMPTY)
	if 'B' in line:
		init_b_pos = [x, line.index('B')]
		line = line.replace('B', EMPTY)
	g_map.append(line)

class Finished(Exception):
	pass

class NoWayBlue(Exception):
	pass

class TooMuchDepth(Exception):
	pass

class State(object):
	def __init__(self, l_pos, move):
		# l_pos is tuple, [0] - red, [1] - blue
		self.l_pos = l_pos
		self.prev_move = move

	def move(self, direction):
		# print("move is called with %s, l_pos: %r" % (str(direction), self.l_pos))

		def is_valid_move():
			if direction == self.prev_move:
				return False
			if direction == UP and self.prev_move == DOWN:
				return False
			if direction == RIGHT and self.prev_move == LEFT:
				return False
			if direction == DOWN and self.prev_move == UP:
				return False
			if direction == LEFT and self.prev_move == RIGHT:
				return False

			return True

		if not is_valid_move():
			return None, False

		if direction == UP:
			color = 1 if self.l_pos[0][0] > self.l_pos[1][0] else 0
		elif direction == DOWN:
			color = 0 if self.l_pos[0][0] > self.l_pos[1][0] else 1
		elif direction == RIGHT:
			color = 0 if self.l_pos[0][1] > self.l_pos[1][1] else 1
		elif direction == LEFT:
			color = 1 if self.l_pos[0][1] > self.l_pos[1][1] else 0

		red_in_hole = False
		blue_in_hole = False

		new_pos, r, b = self.__move_internal(color, self.l_pos, direction)
		red_in_hole |= r
		blue_in_hole |= b
		
		new_pos, r, b = self.__move_internal((color+1)%2, new_pos, direction)
		red_in_hole |= r
		blue_in_hole |= b

		if blue_in_hole:
			raise NoWayBlue
		if red_in_hole:
			raise Finished

		return State(new_pos, direction), True

	def __move_internal(self, color, cur_l_pos, direction):
		# print("__move_internal is called with color: %r, cur_pos: %r, direction: %s" % (color, cur_l_pos, str(direction)))
		pos = cur_l_pos[color][:]
		prev_pos = INVALID_POS

		red_in_hole = False
		blue_in_hole = False

		# Not Wall and Not other color ball
		while g_map[pos[0]][pos[1]] != WALL and pos != cur_l_pos[(color+1)%2]:
			if color == 0 and g_map[pos[0]][pos[1]] == HOLE:
				red_in_hole = True
				prev_pos = INVALID_POS
				break
			if color == 1 and g_map[pos[0]][pos[1]] == HOLE:
				blue_in_hole = True
				prev_pos = INVALID_POS
				break
			prev_pos = pos[:]	
			pos[0] += direction[0]
			pos[1] += direction[1]

		ret_pos = [None, None]
		ret_pos[(color+1)%2] = cur_l_pos[(color+1)%2][:]
		ret_pos[color] = prev_pos

		# print("return pos: %r" % ret_pos)
		return ret_pos, red_in_hole, blue_in_hole

	def __eq__(self, s):
		return self.l_pos[0] == s.l_pos[0] and self.l_pos[1] == s.l_pos[1]

	def __repr__(self):
		return "r: (%d, %d), b: (%d, %d)" % (self.l_pos[0][0], self.l_pos[0][1], self.l_pos[1][0], self.l_pos[1][1])


dir_tuple = (UP, DOWN, RIGHT, LEFT)
states = list()

q = deque()

init_state = State([init_r_pos, init_b_pos], None)
states.append(init_state)

q.append(init_state)
q.append(None)	# for depth of BFS

depth = 1

try:
	while True:
		current_state = q.popleft()
		if not current_state:
			depth += 1
			if depth > 10:
				raise TooMuchDepth
			if len(q) == 0:
				break

			q.append(None)
			current_state = q.popleft()
	
		for d in dir_tuple:
			try:
				# print("Do Move---------------------")
				s, valid = current_state.move(d)
				# print("%r -> %r, direction: %r" % (current_state, s, d))
				# print("valid: %r" % valid)
				if not valid:
					pass
				elif s not in states:
					q.append(s)
			except NoWayBlue:
				# print("Blue hole ...")
				pass

except Finished:
	print(depth)
except TooMuchDepth:
	print(-1)
else:
	print(-1)
