n = int(input())

pay_list = [0 for _ in range(n+1)]

# 1 ~ n
for i in range(1, n+1):
	term, pay = map(int, input().split())
	end_day = i + term - 1
	pay_list[i] = max(pay_list[:i+1])

	if end_day > n:
		continue

	pay_list[end_day] = max(pay_list[end_day], pay_list[i-1] + pay)

print(max(pay_list))
