p_string = input()

class CountDict():
	def __init__(self):
		self.__container = dict()

	def __getitem__(self, key):
		if key in self.__container:
			return self.__container[key]
		else:
			return 0
	def __setitem__(self, key, value):
		self.__container[key] = value
	
	def __repr__(self):
		return str(self.__container)

# stack for save p.
s = list()
# dict for save tmp val for each level
level_table = CountDict()

calc_level = 0
for p in p_string:
	
	if p == '(' or p == '[':
		s.append(p)
		continue

	if len(s) == 0:
		level_table[1] = 0
		break

	current_level = len(s)
	top = s[current_level - 1]

	if p == ')' and len(s) != 0:
		if top == '(':
			if calc_level <= current_level:
				level_table[current_level] += 2
			else:
				calc_val = level_table[calc_level]
				level_table[calc_level] = 0
				level_table[current_level] += calc_val * 2
			s.pop()
			calc_level = current_level
		else:
			level_table[1] = 0
			break
	elif p == ']' and len(s) != 0:
		if top == '[':
			if calc_level <= current_level:
				level_table[current_level] += 3
			else:
				calc_val = level_table[calc_level]
				level_table[calc_level] = 0
				level_table[current_level] += calc_val * 3
			s.pop()
			calc_level = current_level
		else:
			level_table[1] = 0
			break
	else:
		level_table[1] = 0
		break

# invalid p_string
if len(s) != 0:
	level_table[1] = 0

print(level_table[1])

