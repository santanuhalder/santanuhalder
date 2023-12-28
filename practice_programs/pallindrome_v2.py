def is_pallin(txt, start, end):
	while end >= start:
		if txt[start] != txt[end]:
			return False
		start += 1
		end -= 1
	return True


def pallindrome(input_str):
	start, end = 0, len(input_str) - 1
	while end >= start:
		if input_str[start] != input_str[end]:
			return is_pallin(input_str, start + 1, end) or is_pallin(input_str, start, end - 1)
		start += 1
		end -= 1
	return True



input_str1 = 'madam'
input_str2 = 'racecar'
input_str3 = 'madame'

print(is_pallin(input_str1, 0, len(input_str1) - 1))
print(is_pallin(input_str2, 0, len(input_str2) - 1))
print(is_pallin(input_str3, 0, len(input_str3) - 1))

input_str4 = 'racecarzy'
print(pallindrome(input_str4))

