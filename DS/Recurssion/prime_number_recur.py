def is_prime(num):
	if num < 2:
		return False
	if num == 2:
		return True
	return check_divisor(num, 2)


def check_divisor(num, divisor):
	if divisor > num ** 0.5:
		return True
	if num % divisor == 0:
		return False
	return check_divisor(num, divisor + 1)



def prime_checker(num, divisor):
	if num < 2:
		return False
	if num == 2:
		return True
	if divisor is not None:
		if divisor > num ** 0.5:
			return True
		if num % divisor == 0:
			return False
	return prime_checker(num, divisor + 1)

print(is_prime(7))
print(is_prime(12))
print(is_prime(23))
print(is_prime(50))



print(prime_checker(7, 2))
print(prime_checker(12, 2))
print(prime_checker(23, 2))
print(prime_checker(50, 2))

