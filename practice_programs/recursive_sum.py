def sum_array(arr: list) -> int:
    if arr == []:
        return 0
    return arr[0] + sum_array(arr[1:])


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum_array([1,7,3]))



arr = [3]
print(arr[1:])
