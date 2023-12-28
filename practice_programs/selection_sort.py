from fine_smallest_number import find_smallest


def selection_sort(arr) -> list:
    """
    This function sorts an array in ascending order
    :param arr:
    :return:
    """
    new_array = []
    for i in range(len(arr)):
        smallest_number_index = find_smallest(arr)
        new_array.append(arr.pop(smallest_number_index))
    return new_array


number_list = [1, 4, 89, 5, 0, 5, 6]
print(selection_sort(number_list))





