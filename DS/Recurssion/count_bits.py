def count_bits(num):
	if num == 0:
		return 0
	count = num & 1
	num >>= 1
	return count_bits(num) + count

n = 57
print(count_bits(n))