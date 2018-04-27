import heapq
import sys


test_case = int(sys.stdin.readline())

class Casher(object):
	def __init__(self, max_item, per_item, after):
		self.max_item = max_item
		self.per_item = per_item
		self.after = after

# eariliest time
def print_output(i, output):
	sys.stdout.write("Case #%d: %d\n" % (i+1, output))

def work():
	# R, B, C
	r, bit, casher = map(int, sys.stdin.readline().split())

	cashers = list()
	max_time = 0 
	for _ in range(casher):
		# M, S, P
		max_item, per_item, after = map(int, sys.stdin.readline().split())
		cashers.append(Casher(max_item, per_item, after))
		time = after + bit * per_item
		if time > max_time:
			max_time = time

	# Casher can deal with x Bit in T time.
	def capacity(c, t):
		return max(0, min(c.max_item, (t-c.after) // c.per_item))
	
	# Given time, return max handled_bit
	def handled_bit(t):
		heap = list()
		for c in cashers:
			heapq.heappush(heap, -capacity(c, t))

		handled_bits = 0
		counted_r = 0

		while counted_r < r:
			handled_bits += -heapq.heappop(heap)
			counted_r += 1

		return handled_bits

	left = 0
	right = max_time+1

	# Do binary search
	while left < right:
		mid = (left + right) >> 1
		b = handled_bit(mid)
		
		if b < bit:
			left = mid+1
		else:
			right = mid
	
	return right

for i in range(test_case):
	print_output(i, work())

