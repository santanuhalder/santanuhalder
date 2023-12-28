def checkSubarraySum(nums: list, k: int) ->bool:
    """
    Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
    A good subarray is a subarray where: its length is at least two, and the sum of the elements of the subarray is a
    multiple of k. Note that:
    A subarray is a contiguous part of the array.
    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
    :param nums:
    :param k:
    :return:

    Input: nums = [23,2,4,6,7], k = 6
    Output: true
    Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
    """
    remainder = {0: -1} # map remaoinder -> end index
    total = 0

    for i, n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
            remainder[r] = i
        elif i - remainder[r] > 1:
            return True
    return False


nums = [23,2,4,6,7]
k = 7
print(checkSubarraySum(nums, k))

