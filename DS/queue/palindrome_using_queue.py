def is_palindrome(input_string):
    from collections import deque
    q = deque()
    output_string = ''

    for char in input_string:
        q.append(char)
        print(q)
    while len(q) > 1:
        print("Pop left -> {}".format(q.popleft()), end=' ')
        print("Pop right -> {}".format(q.pop()))
        left_ele = q.popleft()
        right_ele = q.pop()
        if left_ele != right_ele:
            return False
    return True

x = "madax"
print(is_palindrome(x))