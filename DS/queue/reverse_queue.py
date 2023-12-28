def reverse_queue(queue):
    stack = list()
    while queue:
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    return queue






q = [1, 2, 3, 4, 5]
print(q)
print(reverse_queue(q))
