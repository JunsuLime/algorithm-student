from collections import deque

height, width = map(int, input().split())

GOOD = 1
EMPTY = -1
NOT_YET = 0

effects = ((1,0), (-1, 0), (0, 1), (0, -1))

t_locations = list()
t_map = list()

def print_map():
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	for line in t_map:
		print(line)
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

for x in range(width):
	line = list(map(int, input().split()))
	t_map.append(line)
	for y, t in enumerate(line):
		if t == GOOD:
			t_locations.append((x, y))


q = deque()
for t_l in t_locations:
	q.append(t_l)

q.append(None)

depth = 0

while True:
	cur_t = q.popleft()
	if not cur_t:
		if len(q) == 0:
			break
		depth += 1
		q.append(None)
		cur_t = q.popleft()
	
	
	for effect in effects:
		x = cur_t[0] + effect[0]
		y = cur_t[1] + effect[1]

		if 0 <= x < width and 0 <= y < height and t_map[x][y] == NOT_YET:
			t_map[x][y] = GOOD
			q.append((x, y))


all_success = True
for line in t_map:
	for t in line:
		if t == NOT_YET:
			all_success = False
			break

if all_success:
	print(depth)
else:
	print(-1)

