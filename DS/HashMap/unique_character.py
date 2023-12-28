def unique_char(txt):
	freq = dict()

	for char in txt:
		freq[char] = freq.setdefault(char, 0) + 1

	for i, char in enumerate(txt):
		if freq[char] == 1:
			return i
	return -1

txt1 = "abcab"
print(unique_char(txt1))

