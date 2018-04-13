# Tetromino

tetromino = (
				# expect s, represent all other a with tuples.

				# saaa
				((1, 0), (2, 0), (3, 0)),
				((0, 1), (0, 2), (0, 3)),
				
				# sa   s    aa   a
				#  aa  aa  sa   aa   
				#       a       s
				((0, 1), (1, 1), (1, 2)),
				((1, 0), (1, 1), (2, 1)),
				((0, 1), (-1, 1), (-1, 2)),
				((-1, 0), (-1, 1), (-2, 1)),

				# sa
				# aa
				((1, 0), (0, 1), (1, 1)),

				# s     a    a
				# aa   saa  sa   saa
				# a          a    a
				((1, 0), (2, 0), (1, 1)),
				((0, 1), (-1, 1), (0, 2)),
				((0, 1), (1, 1), (-1, 1)),
				((0, 1), (0, 2), (1, 1)),

				# s   saa    sa    saa    a  sa    a  s
				# a   a      a       a    a   a  saa  aaa
				# aa         a           sa   a
				((1, 0), (2, 0), (2, 1)),
				((1, 0), (0, 1), (0, 2)),
				((0, 1), (1, 0), (2, 0)),
				((0, 1), (0, 2), (1, 2)),
				((0, 1), (-1, 1), (-2, 1)),
				((0, 1), (1, 1), (2, 1)),
				((0, 1), (0, 2), (-1, 2)),
				((1, 0), (1, 1), (1, 2)),
			)

row, col = map(int, input().split())

num_map = list()
for _ in range(row):
	num_map.append(list(map(int, input().split())))

max_val = 0

for i in range(row):
	for j in range(col):
		for t in tetromino:
			sum_val = num_map[i][j]
			valid_t = True
			for p in t:
				point_x = i + p[0]
				point_y = j + p[1]
				if not (0 <= point_x < row and 0 <= point_y < col):
					valid_t = False
					break
				
				sum_val += num_map[point_x][point_y]

			if valid_t and sum_val > max_val:
				max_val = sum_val

print(max_val)

					



