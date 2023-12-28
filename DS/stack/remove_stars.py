def remove_stars(input_str):
    stack = list()
    for char in input_str:
        if stack and char == '*':
            stack.pop()
        elif stack and stack[-1] == '*':
            stack.pop()
        elif char == '*':
            pass
        else:
            stack.append(char)
    return ''.join(stack)


input_str1 = "a**b*c*d"  # 'abc', 'de', 'f'
input_str2 = "a*b*c*d"  # 'abc', 'de', 'f'
input_str3 = "abcd"
print(remove_stars(input_str1))
# print(remove_stars(input_str2))
# print(remove_stars(input_str3))