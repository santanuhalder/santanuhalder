def sort_by_freq(s: str) -> str:
	freq = dict()
	res = ""
	for char in s:
		freq[char] = freq.setdefault(char, 0) + 1
	frequencies = [v for v in freq.values()]

	frequencies.sort(reverse=True)
	counter = 0
	heap_len = len(frequencies)

	while counter < heap_len:
		current_max_freq = frequencies[counter]
		curr_char_list = [k for k, v in freq.items() if v == current_max_freq]
		for i in range(len(curr_char_list)):
			res += curr_char_list[i]*current_max_freq
			counter += 1
	return res

s1 = "tree"
s2 = "cccaaa"
s3 = "Aabb"
s4 = "tee"
s5 = "loveleetcode"

print(sort_by_freq(s1))
print(sort_by_freq(s2))
print(sort_by_freq(s3))
print(sort_by_freq(s4))
print(sort_by_freq(s5))