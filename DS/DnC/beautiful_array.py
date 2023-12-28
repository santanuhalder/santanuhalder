def beautiful_array(num):
	if num == 1:
		return [1]

	even = beautiful_array(num // 2)
	odd = beautiful_array((num + 1) // 2)

	return [2*x for x in even] + [2*x - 1 for x in odd]

n = 8
res = beautiful_array(n)

print(res)