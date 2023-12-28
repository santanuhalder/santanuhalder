def max_diff(input_list):
    """
    Maximum difference between two elements such that larger element appears after the smaller number
    Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element
    appears after the smaller number.
    Examples :
    Input : arr = {2, 3, 10, 6, 4, 8, 1}
    Output : 8
    Explanation : The maximum difference is between 10 and 2.
    """
    diff = 0

    for i in range(0, len(input_list)):
        for j in range(i + 1, len(input_list)):
            diff = max(diff, input_list[j] - input_list[i])

    return diff


def difference(input_list):
    minElement = input_list[0]
    diff = input_list[1] - input_list[0]

    for i in range(1, len(input_list)):
        diff = max(diff, input_list[i] - minElement)
        if input_list[i] < minElement:
            minElement = input_list[i]
    return diff


arr = [20, 3, 2, 6, 4, 8, 1]
print(difference(arr))
#print(max_diff(arr))
