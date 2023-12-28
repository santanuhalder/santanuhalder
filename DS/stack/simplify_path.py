def simplify_path(path):
    stack = list()
    path_list = path.split('/')
    for char in path_list:
        if (char == '' or char == '.') or (not stack and char == '..'):
            pass
        elif stack and char == '..':
            stack.pop()
        else:
            stack.append(char)
    return '/' + '/'.join(stack)


input = "/a//b////c/d//././/.."
input1 = "/../"
input2 = "/home//foo/"
input3 = "/../"
print(simplify_path(input3))
print(input.split('/'))