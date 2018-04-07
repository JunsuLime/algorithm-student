test_case = int(input())

class ChargeShoot(object):
	def __init__(self, charge, shoot):
		self.charge = charge
		self.shoot = shoot

	def __repr__(self):
		return "{charge: %d, shoot: %d}" % (self.charge, self.shoot)
	

def print_output(i, result):
	if type(result) is str:
		print("Case #%d: %s" % (i+1, result))
	else:
		print("Case #%d: %d" % (i+1, result))

def work():
	shield, program = input().split()
	shield = int(shield)

	# print("----------------------------------")
	# print(shield, program)

	if shield < program.count("S"):
		return "IMPOSSIBLE"
	
	charge_count = 0
	shoot_count = 0

	cs_list = list()

	""" Build cs_list custom data structure start """
	prev_instruction = None
	for instruction in program:
		if instruction == "C":
			if prev_instruction == "S":
				cs_list.append(ChargeShoot(charge_count, shoot_count))
				charge_count = 0
				shoot_count = 0
			charge_count += 1
		elif instruction == "S":
			shoot_count += 1

		prev_instruction = instruction
	
	if shoot_count != 0:
		cs_list.append(ChargeShoot(charge_count, shoot_count))
	""" Build cs_list custom data structure end """
	
	def current_attack():
		stacked_charge = 0
		sum_attack = 0
		
		for cs in cs_list:
			c = cs.charge
			s = cs.shoot

			stacked_charge += c
			charged_attack = 1 << (stacked_charge)
			sum_attack += s * charged_attack
		
		if len(cs_list) != 0:
			last_cs = cs_list[len(cs_list)-1]
			last_charge = 1 << stacked_charge
		else:
			last_cs = None
			last_charge = 0

		return sum_attack, last_charge, last_cs
	
	swap_count = 0
	
	while True:
		sum_attack, last_charge, last_cs = current_attack()
		# print(shield, sum_attack, last_charge, last_cs)
		# print("current swap_count: %d" % swap_count)
		# print(cs_list)
		if sum_attack <= shield:
			break

		# if last cs reduce all c -> remained shield
		remained_shield = shield - (sum_attack - ((last_charge * last_cs.shoot) >> 1))
		# print("remained shield: %d" % remained_shield)
		if remained_shield < 0:
			swap_count += last_cs.shoot
			last_cs.charge -= 1
			if last_cs.charge == 0:
				cs_list.pop()
				cs_list[len(cs_list)-1].shoot += last_cs.shoot
		else:
			except_last_attack = sum_attack - (last_charge * last_cs.shoot)
			remained_shield = shield - except_last_attack
			# print("except_last_attack: %d, remained_sheild: %d" % (except_last_attack, remained_shield))

			swap_count += 2 * last_cs.shoot - (remained_shield // (last_charge >> 1))
			break

	return swap_count


for i in range(test_case):
	print_output(i, work())

