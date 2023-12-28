def max_sub_array(num, k):
    res = list()
    i = 0

    max_ele = num[0]
    for j in range(1, k):
        max_ele = max(max_ele, num[j])

    res.append(max_ele)

    while k < len(num):
        max_ele = max(max_ele, num[k])
        res.append(max_ele)
        k += 1

    return res


def max_sub_array_queue(num, k):
    from collections import deque
    queue = deque()
    max_ele = num[0]
    res = list()

    for i in range(0, k):
        max_ele = max(max_ele, num[i])

    queue.appendleft(max_ele)
    res.append(max_ele)

    while queue:
        max_ele = max(max_ele, queue.pop())




input_num1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
input_num2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
input_num3 = [1, 2, 3, 4, 5]
m = 3
print(max_sub_array(input_num3, m))



