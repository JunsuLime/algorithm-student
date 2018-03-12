from collections import deque

n, stride = map(int, input().split())
stride = stride - 1
q = deque(list(range(1, n+1)))

result = list()

while len(q) != 0:
	q.rotate(-stride)
	result.append(q.popleft())

result = str(result)
result = result.replace('[', '<').replace(']', '>')

print(result)

