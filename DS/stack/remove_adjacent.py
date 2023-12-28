def remove_adjacent(input):
    stack = list()
    for char in input:
        if stack and (stack[-1] == char):
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)



input_str = "abbaca" # ca
input_str2 = "azxxzy"
input_str3 = "abba"
print(remove_adjacent(input_str))
print(remove_adjacent(input_str2))
print(remove_adjacent(input_str3))
