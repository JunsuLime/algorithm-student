# Time complexity: O(
# Elapsed time: 48ms
#
# Complete search, Recursion
# 
# 1) if all pairs are matched -> return 1 (+1)
# 2) if not friend match occur -> return 0 (None)
# 3) else, keep going matching !

import itertools


test_case = int(input())


def work():
	# s_num: student number, p_num: pair num
	s_num, p_num = map(int, input().split())

	# make list of set length student number
	# this will save friend ship
	# like 0's friend: friend_map[0] = {1, 2, 4}
	friend_map = [set() for _ in range(s_num)]

	# enumerate - (idx, element) iteration
	current_base = 0
	for idx, s in enumerate(map(int, input().split())):
		if idx % 2 == 0:
			current_base = s
		else:
			# if a is b's friend, b is a's friend too.
			friend_map[current_base].add(s)
			friend_map[s].add(current_base)
	
	def matching():
		"""
		return number of matching case.
		"""
		def __matching_internal(m, tried_pair):
			"""
			return match_count of current state (tried_pair)
			
			@param m: current base matcher
			@return: match count
			"""
			# if all pair is mathed -> return 1: success
			if len(tried_pair) == s_num:
				return 1
			# if match base is already matched student -> return 0: failure
			if m in tried_pair:
				return 0

			match_count = 0
			# only m's friend can be matched
			for f in friend_map[m]:
				if f in tried_pair:
					continue
				tried_pair.add(m)
				tried_pair.add(f)
				next_m = m+1
				while next_m in tried_pair:
					next_m += 1
				# get fastest number matchable friend
				match_count += __matching_internal(next_m, tried_pair)
				tried_pair.remove(m)
				tried_pair.remove(f)

			return match_count
	
		# start matching work from 0
		return __matching_internal(0, set())
	
	return matching()


for _ in range(test_case):
	print(work())

