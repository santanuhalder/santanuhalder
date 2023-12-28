def min_add(s):
	balance, counter = 0, 0
	for char in s:
		if char == '(':
			balance += 1
		else:
			balance -= 1
		if balance == -1:
			counter += 1
			balance += 1
	return counter + balance


input_string1 = "(()"
input_string2 = "))(("
input_string3 = "(()())("

print(min_add(input_string1))
print(min_add(input_string2))
print(min_add(input_string3))