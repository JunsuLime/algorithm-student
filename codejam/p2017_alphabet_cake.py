import sys

test_case = int(input())

UP = 3
RIGHT = 2
DOWN = 1
LEFT = 0

class Rect(object):
	def __init__(self, lt, rb, element):
		self.lt = lt
		self.rb = rb
		self.element = element

	def __repr__(self):
		return "%r %r %r" % (self.lt, self.rb, self.element)
		

def print_output(idx, output):
	print("Case #%d:" % (idx+1))
	for line in output:
		for e in line:
			sys.stdout.write(e)
		sys.stdout.write('\n')


def work():
	row, col = map(int, input().split())
	rect_list = list()

	cake = list()
	for x in range(row):
		line = list(input())
		cake.append(line)

		for y, e in enumerate(line):
			if e == '?':
				continue
			rect_list.append(Rect([x, y], [x, y], e))
	
	for move in range(4):
		for base_rect in rect_list:
			b_up = base_rect.lt[0]
			b_left = base_rect.lt[1]
			b_bottom = base_rect.rb[0]
			b_right = base_rect.rb[1]

			u_up = b_up
			u_left = b_left
			u_bottom = b_bottom
			u_right = b_right

			if move == UP:
				u_up = 0
			elif move == DOWN:
				u_bottom = row - 1
			elif move == RIGHT:
				u_right = col - 1
			elif move == LEFT:
				u_left = 0
			
			for comp_rect in rect_list:
				if base_rect is comp_rect:
					continue
				c_up = comp_rect.lt[0]
				c_left = comp_rect.lt[1]
				c_bottom = comp_rect.rb[0]
				c_right = comp_rect.rb[1]

				if move == UP:
					if b_right < c_left or b_left > c_right:
						u_up = max(u_up, 0)
					elif b_up > c_bottom:
						u_up = max(u_up, c_bottom + 1)
				elif move == DOWN:
					if b_right < c_left or b_left > c_right:
						u_bottom = min(u_bottom, row - 1)
					elif b_bottom < c_up:
						u_bottom = min(u_bottom, c_up - 1)
				elif move == RIGHT:
					if b_up > c_bottom or b_bottom < c_up:
						u_right = min(u_right, col - 1)
					elif b_right < c_left:
						u_right = min(u_right, c_left - 1)
				elif move == LEFT:
					if b_up > c_bottom or b_bottom < c_up:
						u_left = max(u_left, 0)
					elif b_left > c_right:
						u_left = max(u_left, c_right + 1)


			base_rect.lt[0] = u_up
			base_rect.lt[1] = u_left
			base_rect.rb[0] = u_bottom
			base_rect.rb[1] = u_right

	# after 4 direction moves
	# put rect on cake.

	for rect in rect_list:
		# draw rect info on cake
		for x in range(rect.lt[0], rect.rb[0]+1):
			for y in range(rect.lt[1], rect.rb[1]+1):
				cake[x][y] = rect.element
	
	return cake

for i in range(test_case):
	print_output(i, work())

