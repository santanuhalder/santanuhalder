def qsort_p(nums: list) -> list:
    """

    :param nums:
    :return:
    """
    if len(nums) < 2:
        return nums
    else:
        pivot = len(nums) // 2
        lower = [i for i in nums[0:pivot] if i <= nums[pivot]] + [i for i in nums[pivot+1:] if i <= nums[pivot]]
        higher = [i for i in nums[0:pivot] if i >= nums[pivot]] + [i for i in nums[pivot+1:] if i >= nums[pivot]]
        return qsort_p(lower) + [nums[pivot]] + qsort_p(higher)

numbers = [1, 4, 2, 9, 10, 0]
print(qsort_p(numbers))