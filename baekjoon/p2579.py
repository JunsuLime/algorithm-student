num_stairs = int(input())

point_l = list()
point_l.append(0)
for _ in range(num_stairs):
	point_l.append(int(input()))


max_point = [[0, 0] for _ in range(num_stairs+1)]
max_point[1] = [point_l[1], point_l[1]]

for i in range(2, num_stairs+1):
	c1 = max_point[i-1]
	c2 = max_point[i-2]

	max_point[i][0] = point_l[i] + c1[1]
	max_point[i][1] = point_l[i] + max(c2[0], c2[1])

print(max(max_point[num_stairs]))


