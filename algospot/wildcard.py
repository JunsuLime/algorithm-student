import sys
import heapq

STAR = '*'
QUESTION = '?'
UNKNOWN = -1

test_case = int(sys.stdin.readline())


def build_nfa(regex):
	pass

def build_dfa(nfa):
	pass

def work():
	# FSA
	regexp = sys.stdin.readline().rstrip()
	
	# finish state, True - right exp, False - wrong exp
	# build FSA (Finite State Automata)
	nfa = build_nfa(regexp)
	dfa = build_dfa(nfa)
	
	success = list()

	file_num = int(sys.stdin.readline())
	for _ in range(file_num):
		file_name = sys.stdin.readline().rstrip()
		pass

	while success:
		sys.stdout.write('%s\n' % heapq.heappop(success))

def work_well():
	regexp = sys.stdin.readline().rstrip()

	heap = list()
	file_num = int(sys.stdin.readline())
	for _ in range(file_num):
		file_name = sys.stdin.readline().rstrip()

		cached = [[UNKNOWN for _ in range(len(file_name))] for _ in range(len(regexp))]

		s = list()
		# first is regexp's idx, and second is matching string's idx
		s.append((0, 0))

		valid = False
		while s:
			r_idx, s_idx = s.pop()
			if r_idx == len(regexp) and s_idx == len(file_name):
				valid = True
				break
			if not (0 <= r_idx < len(regexp)+1 and 0 <= s_idx < len(file_name)+1):
				continue
			
			r_ch = regexp[r_idx] if r_idx < len(regexp) else None
			s_ch = file_name[s_idx] if s_idx < len(file_name) else None
			if r_ch == STAR:
				s.append((r_idx+1, s_idx+1))
				s.append((r_idx, s_idx+1))
				s.append((r_idx+1, s_idx))
			elif r_ch == QUESTION:
				s.append((r_idx+1, s_idx+1))
			else:
				if s_ch == r_ch:
					s.append((r_idx+1, s_idx+1))

		if valid:
			heapq.heappush(heap, file_name)
	
	while heap:
		sys.stdout.write("%s\n" % heapq.heappop(heap))


for _ in range(test_case):
	work_well()
