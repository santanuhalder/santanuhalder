def count_bits(txt):
	num = 0
	for x in txt:
		num += 1 & int(x)
	return num


def num_bits(b):
	print(b << 1)


s = "11111111111111111111111111111101"

n = 10
b = bin(10)


print(num_bits(b))
