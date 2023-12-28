def remove_duplidate_from_list(nums: list) -> list:
    """

    :param nums:
    :return:
    """
    res = list()
    res.append(nums[0])
    i, j = 1, 1

    while j < len(nums):
        if res[i-1] != nums[j]:
            res.append(nums[j])
            i += 1
            j += 1
        else:
            j += 1
    return res

numbers = [1, 1, 2, 3, 3, 5, 5]
print(remove_duplidate_from_list(numbers))

