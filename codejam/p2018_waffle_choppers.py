test_case = int(input())

IMPOSSIBLE = 'IMPOSSIBLE'
POSSIBLE = 'POSSIBLE'

CHOCO = '@'

def print_output(i, output):
	print('Case #%d: %s' % (i+1, output))

def work():
	row, col, h_cut, v_cut = map(int, input().split())
	
	w_map = list()
	total_c = 0
	for _ in range(row):
		line = input()
		w_map.append(line)
		total_c += line.count(CHOCO)

	if total_c == 0:
		return POSSIBLE

	h_div = h_cut + 1
	v_div = v_cut + 1

	# In this observation, we can determine IMPOSSIBLE easily. So powerful
	if total_c % h_div != 0 or total_c % v_div != 0:
		return IMPOSSIBLE
	
	row_sum = total_c // h_div
	col_sum = total_c // v_div
	cell_sum = row_sum // v_div

	# all range representation is half-opened range [start, end)
	div_rows = list()
	div_cols = list()
	div_rows.append(0)
	div_cols.append(0)

	# Build div rows
	p_sum = 0
	for x, row in enumerate(w_map):
		p_sum += row.count(CHOCO)
		if p_sum == row_sum:
			div_rows.append(x+1)
			p_sum = 0
		# In case that div row cannot be done
		elif p_sum > row_sum:
			return IMPOSSIBLE

	
	# Build col rows
	p_sum = 0
	for y in range(col):
		for x in range(len(w_map)):
			if w_map[x][y] == CHOCO:
				p_sum += 1

		if p_sum == col_sum:
			p_sum = 0
			div_cols.append(y+1)
		# In case that div col cannot be done
		elif p_sum > col_sum:
			return IMPOSSIBLE
	
	
	# Solve problem... through dividing waffle -> fair division OK?
	for i in range(len(div_rows)-1):
		row_start = div_rows[i]
		row_end = div_rows[i+1]
		for j in range(len(div_cols)-1):
			col_start = div_cols[j]
			col_end = div_cols[j+1]

			chocolate_count = 0
			for x in range(row_start, row_end):
				for y in range(col_start, col_end):
					if w_map[x][y] == CHOCO:
						chocolate_count += 1

			# If chocolate count is not same as expected count
			# then return IMPOSSIBLE
			if chocolate_count != cell_sum:
				return IMPOSSIBLE
	# If pass on all case -> POSSIBLE with div_cols, div_rows
	return POSSIBLE

for t in range(test_case):
	print_output(t, work())
