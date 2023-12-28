def longest_parenthesis(s):
	max_length = 0
	p = {')': '('}
	stack = []

	for char in s:
		if char not in p:
			stack.append(char)
		else:
			if stack and stack[len(stack) - 1] == p[char]:
				stack.pop()
				max_length += 2
	return max_length

input_str1 = "(())" # 4
input_str2 = ")()())" # 4
input_str3 = "(()" # 2
input_str4 = "(()(()" # 2
print(longest_parenthesis(input_str1))
print(longest_parenthesis(input_str2))
print(longest_parenthesis(input_str3))
print(longest_parenthesis(input_str4))
