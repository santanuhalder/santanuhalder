def generate_binary_numbers(num):
    from collections import deque
    q = deque()
    res = list()
    q.appendleft("1")

    while num > 0:
        lastitem = q.pop()
        res.append(lastitem)
        s1 = lastitem + "0"
        s2 = lastitem + "1"
        q.appendleft(s1)
        q.appendleft(s2)
        num -= 1
    return res

# Testing
print(generate_binary_numbers(5))
# print(generate_binary_numbers(3))
# print(generate_binary_numbers(5))
