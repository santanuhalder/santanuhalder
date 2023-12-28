def find_smallest(arr: list) -> int:
    """
    This function goes through an array arr and return the index of the smallest number
    :param arr: input array
    :return: return the index of the smallest number
    """
    smallest_number = arr[0]
    smallest_number_index = 0
    for i in range(1, len(arr)):
        if smallest_number < arr[i]:
            smallest_number = arr[i]
            smallest_number_index = i
    return smallest_number_index


number_list = [23, 10, 5, 9, 8]

if __name__ == "__main__":
    print(find_smallest(number_list))
