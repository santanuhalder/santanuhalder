from collections import Counter
def remove_duplicates(s):
	char_count = {char: s.count(char) for char in set(s)}
	present = set()
	result = list()

	for char in s:
		if char not in present:
			while result and char < result[-1] and char_count[result[-1]] > 0:
				present.remove(result.pop())
			result.append(char)
			present.add(char)
		char_count[char] -= 1
	return ''.join(result)

input_string1 = "bbaac"
input_string2 = "zabccdef"
input_string3 = "mnopmn"
input_string4 = "bcabc"

print(remove_duplicates(input_string1))
print(remove_duplicates(input_string2))
print(remove_duplicates(input_string3))
print(remove_duplicates(input_string4))
