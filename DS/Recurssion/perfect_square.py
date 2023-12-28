def is_perfect_square(num):
	if num == 0 or num == 1:
		return True
	return perfect_square(num, 0, num)


def perfect_square(num, low, high):
	if high >= low:
		mid = (high + low) // 2

		if mid * mid == num:
			return True
		elif mid * mid > num:
			return perfect_square(num, low, mid - 1)
		else:
			return perfect_square(num, mid + 1, high)
	else:
		return False


print(is_perfect_square(2))


