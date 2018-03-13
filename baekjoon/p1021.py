from collections import deque


n, pick_count = map(int, input().split())
queue = deque(list(range(1, n+1)))
pick_queue = deque(list(map(int, input().split())))

rotate_count = 0

while len(pick_queue) != 0:
	# print("pick_queue: %r" % pick_queue)
	pick_item = pick_queue.popleft()

	index = -1
	for idx, item in enumerate(queue):
		if item == pick_item:
			index = idx
			break

	# print("index: %r, item: %r" % (index, pick_item))
	# print("before rotate: %r" % queue)

	left = index
	right = len(queue) - index

	if left < right:
		queue.rotate(-left)
		rotate_count += left
		# print("left %r" % left)
	else:
		queue.rotate(right)
		rotate_count += right
		# print("right %r" % right)

	# print("after rotate: %r" % queue)

	queue.popleft()
	# print("after pop: %r" % queue)
	# print("========================")

print(rotate_count)
	
	
