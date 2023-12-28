def two_sum(nums, target):
	num_map = {}

	for i in range(len(nums)):
		complement = target - nums[i]
		if complement in num_map:
			return [num_map[complement], i]
		num_map[nums[i]] = i

	return []

def twoSum(nums, target):
	d = {num: i for i, num in enumerate(nums)}

	for num in nums:
		if (target - num) in d:
			return [d[num], d[target-num]]
	return []


nums = [2, 7, 11, 15]
d = {num: i for i, num in enumerate(nums)}
print(d)

target = 9

print(two_sum(nums, target))
# Output: [0,1]
print(twoSum(nums, target))