def left_right_sum_difference(nums):
    n = len(nums)
    leftSum = [0]*n
    rightSum = [0]*n
    differenceArray = [0]*n

    leftSum[0] = nums[0]
    for i in range(1, n):
        leftSum[i] = leftSum[i-1] + nums[i]

    rightSum[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        rightSum[i] = rightSum[i+1] + nums[i]

    for i in range(0, n):
        differenceArray[i] = abs(leftSum[i] - rightSum[i])
    return differenceArray

