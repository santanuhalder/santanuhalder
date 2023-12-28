def longest_pallindrome(s: str) -> int:
	freq = {}
	for char in s:
		freq[char] = freq.setdefault(char, 0) + 1

	length = 0
	single_char_count = 0

	for char, val in freq.items():
		if val % 2 == 0:
			length += val
		elif val % 2 == 1:
			length += (val - 1)
			single_char_count += 1
	if single_char_count >= 1:
		length += 1
	return length

input_txt1 = "applepie"
input_txt2 = "aabbcc"
input_txt3 = "bananas"

print(longest_pallindrome(input_txt1))
print(longest_pallindrome(input_txt2))
print(longest_pallindrome(input_txt3))