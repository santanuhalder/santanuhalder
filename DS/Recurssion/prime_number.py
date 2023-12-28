def prime_number(num):
	var = 2
	while var < num:
		if num % var == 0:
			return False
		var += 1
	return True


def prime_number_recur(var):
	if var == 1:
		return False
	elif var == 2:
		return True
	return prime_number()

print(prime_number(7))
print(prime_number(12))
print(prime_number(23))
print(prime_number(50))
