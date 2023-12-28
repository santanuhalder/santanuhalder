list1 = [1, 2, 5, 8, 10]
list2 = [2, 4, 6, 11, 15, 16]

i, j = 0, 0
list1_size = len(list1)
list2_size = len(list2)
result = []

while i < list1_size and j <list2_size:
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

result = result + list1[i:] + list2[j:]

print(result)