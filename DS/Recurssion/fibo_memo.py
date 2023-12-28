def fibbo(num):
	if num <= 1:
		return num
	memo = dict()

	if num in memo:
		return memo[num]
	else:
		result = fibbo(num - 1) + fibbo(num - 2)
		memo[num] = result
	return memo[num]


# 0, 1, 1, 2, 3, 5, 8, 13

print(fibbo(7))