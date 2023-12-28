def longest_substring(s):
	char_set = set()
	length = -float('inf')
	start = 0

	for end in range(len(s)):
		while s[end] in char_set:
			char_set.remove(s[start])
			start += 1
		char_set.add(s[end])
		length = max(length, end - start + 1)
	return length


input_s1 = "abcdaef"
input_s2 = "aaaaa"
input_s3 = "abrkaabcdefghijjxxx"
input_s4 = "abcabcbb"

print(longest_substring(input_s1))
print(longest_substring(input_s2))
print(longest_substring(input_s3))
print(longest_substring(input_s4))
