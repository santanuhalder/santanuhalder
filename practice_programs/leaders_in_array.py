def find_array_leaders(arr):
    """
    Input: arr[] = {16, 17, 4, 3, 5, 2},
    Output: 17, 5, 2

    Input: arr[] = {1, 2, 3, 4, 5, 2},
    Output: 5, 2
    """
    res_array = []
    reverse_max = []
    max_so_far = -float("inf")
    # max_so_far = 0

    # First way
    # for i in range(1, len(arr)):
    #     if arr[i - 1] > max(arr[i:]):
    #         res_array.append(arr[i-1])
    # res_array.append(arr[len(arr) - 1])
    # return res_array

    # Second way
    for i in range(len(arr) - 1, -1, -1):
        max_so_far = max(max_so_far, arr[i])
        if arr[i] >= max_so_far:
            res_array.append(arr[i])
    res_array.reverse()
    return res_array


# nums = [16, 17, 4, 3, 5, 2]
nums = [1, 2, 3, 4, 5, 2, -10]
print(find_array_leaders(nums))
