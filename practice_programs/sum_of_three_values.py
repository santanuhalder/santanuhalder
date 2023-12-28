def find_sum_target(target: int, num_range: int) -> bool:
    """
    Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums
    whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such
    integers exist in the array. Otherwise, return FALSE.

    :param target:
    :param num_range:
    :return:
    """

    for i in range(0, len(test_arr) - num_range + 1):
        low = i + 1
        high = len(test_arr) - 1

        sum = 0
        while low < high:
            sum = test_arr[i] + test_arr[low] + test_arr[high]

            if sum == target:
                return True
            elif sum < target:
                low += 1
            else:
                high -= 1
    return False


test_arr = [1, 3, 4, 6, 7, 20] # index 0, 1, 2, 3, 4, 5  for i in range(0, 4) 6 - 3 + 1  len(test_arr) - range + 1
target_num = 31
k = 3
print(find_sum_target(target_num, k))





