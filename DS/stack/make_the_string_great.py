def make_the_string_great(chars):
    stack = list()
    for char in chars:
        if not stack:
            stack.append(char)
        elif (stack[-1].casefold() == char.casefold()) and (stack[-1] != char):
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


input_str = 'AaBbCcDdEeff'
print(make_the_string_great(input_str))


