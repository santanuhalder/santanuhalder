def sort_a_stack(stack):
    tempStack = []
    while stack:
        element = stack.pop()
        while tempStack and element < tempStack[-1]:
            stack.append(tempStack.pop())
        tempStack.append(element)
    return tempStack





input = [34, 3, 31, 98, 92, 23]
print(sort_a_stack(input))

