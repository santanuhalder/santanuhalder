def jewels_stones(jewels, stones):
	all_jewels = set(jewels)
	count = 0
	for stone in stones:
		if stone in all_jewels:
			count += 1
	return count

jewels1 = "abc"
stones1 = "aabbcc"

jewels2 = "aA"
stones2 = "aAaZz"

jewels3 = "zZ"
stones3 = "zZzZzZ"

print(jewels_stones(jewels1, stones1))
print(jewels_stones(jewels2, stones2))
print(jewels_stones(jewels3, stones3))