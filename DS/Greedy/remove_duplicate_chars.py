def rem_duplicate(s):
	count = {char: s.count(char) for char in set(s)}
	result = list()
	present = set()

	for char in s:
		if char not in present:
			while result and result[-1] > char and count[result[-1]] > 0:
				present.remove(result.pop())
			present.add(char)
			result.append(char)
		count[char] -= 1
	return ''.join(result)


input_txt1 = "bbaac"
input_txt2 = "zabccde"
input_txt3 = "mnopmn"

print(rem_duplicate(input_txt1))
print(rem_duplicate(input_txt2))
print(rem_duplicate(input_txt3))