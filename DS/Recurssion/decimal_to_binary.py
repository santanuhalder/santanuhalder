def dec_to_bin_iter(num):
	txt = ''
	while num > 0:
		txt += str(num % 2)
		num = num // 2
	return txt[::-1]


def dec_to_bin_recur(num):
	if num == 0:
		return ''
	bin_bit = str(num % 2)
	return dec_to_bin_iter(num // 2) + bin_bit

n = 8
print(dec_to_bin_iter(n))

n = 8
print(dec_to_bin_recur(n))