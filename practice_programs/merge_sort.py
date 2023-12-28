def merge_sort(num1: list, num2: list) -> list:
    """
    Function to return merged list of two sorted list input
    :param num1: first sorted input list
    :param num2: second sorted input list
    :return: resutant sorted list
    """

    i, j = 0, 0
    len1, len2 = len(num1), len(num2)
    sorted_list = []
    while i < len1 and j < len2:
        if num1[i] < num2[j]:
            sorted_list.append(num1[i])
            i += 1
        else:
            sorted_list.append(num2[j])
            j += 1
    sorted_list = sorted_list + num1[i:] + num2[j:]
    return sorted_list

list1 = [1, 3, 8, 10, 15, 30]
list2 = [4, 6, 9, 15, 20]

print(merge_sort(list1, list2))

