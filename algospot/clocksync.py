# Time Complexity: O(4^10)
# Elapsed time: Time exceeded .. T_T
#
# Complete search problem
# python is weak for recursive call. when recursion occur a lot.
# avoid using python.

test_case = int(input())

switch = (
			(0, 1, 2),
			(3, 7, 9, 11),
			(4, 10, 14, 15),
			(0, 4, 5, 6, 7),
			(6, 7, 8, 10, 12),
			(0, 2, 14, 15),
			(3, 14, 15),
			(4, 5, 7, 14, 15),
			(1, 2, 3, 4, 5),
			(3, 4, 5, 9, 13),
	     )

# maximum click count is 30
# order of clicking is not important. important thing is 
# how many switch click
# 
# click switch more than 3 times are not meaningful.
# so meaningful switch max click is 3 and there are 10 switch
# max switch click count is 30 and 31 is invalid click count
# if return this value, there is no way to clock sync
INVALID_CLICK = 31
ROTATE = 4

def clock_sync_done(state):
	for c in state:
		if c != 0:
			return False
	return True

def click_count(state, cur):
	"""
	get click_count in this state

	@param state: current state
	@param cur: manuplating switch in this function
	@param click: acculmulated click

	@return: minimum click count in this state
	"""
	if clock_sync_done(state):
		return 0
	if cur == len(switch):
		return INVALID_CLICK

	count = INVALID_CLICK
	for i in range(ROTATE):
		count = min(count, click_count(state, cur+1) + i)	
		for clock_idx in switch[cur]:
			state[clock_idx] = (state[clock_idx]+1) % ROTATE
	
	return count

def work():
	"""
	complete search is needed

	len(switch) == 10, 4 variation of clicking switch
	4 ** 10 is all case count
	"""
	clocks = list()
	# for the easy calculation
	# 12 -> 0, 3 -> 1, 6 -> 2, 9 -> 3
	for t in list(map(int, input().split())):
		if t == 12:
			clocks.append(0)
		else:
			# t // 3 == int(t / 3)
			clocks.append(t // 3)
	
	click = click_count(clocks, 0)
	if click == INVALID_CLICK:
		return -1
	else:
		return click

for _ in range(test_case):
	print(work())
