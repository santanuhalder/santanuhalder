def find_altitude(nums):
    max_altitude = [None]*len(nums)

    max_altitude[0] = nums[0]
    for i in range(1, len(nums)):
        max_altitude[i] = max_altitude[i-1] + nums[i]

    return max(max_altitude)


input = [4, -3, 2, -1, -2]
print(find_altitude(input))




