ASCENDING = 'ascending'
DESCENDING = 'descending'
MIXED = 'mixed'

l = list(map(int, input().split()))

status = None
if l[0] < l[1] < l[2]:
	status = ASCENDING
	for i in range(2, len(l)-1):
		if l[i] < l[i+1]:
			pass
		else:
			status = MIXED

elif l[0] > l[1] > l[2]:
	status = DESCENDING
	for i in range(2, len(l)-1):
		if l[i] > l[i+1]:
			pass
		else:
			status = MIXED
else:
	status = MIXED
print(status)
