def is_there_duplicate(arr):
	freq = dict()
	for num in arr:
		if num in freq:
			return True
		freq[num] = freq.setdefault(num, 0) + 1
	return False

def contains_duplicate(arr):
	arr.sort()
	for i in range(len(arr) - 1):
		if arr[i] == arr[i+1]:
			return True
	return False

def duplicate_using_set(arr):
	num_set = set(arr)
	if len(num_set) != len(arr):
		return True
	return False


nums = [1, 2, 3, 4]
nums1 = [1, 2, 3, 1]
print(is_there_duplicate(nums))
print(is_there_duplicate(nums1))
print("*"*20)
print(contains_duplicate(nums))
print(contains_duplicate(nums1))
print("*"*20)
print(duplicate_using_set(nums))
print(duplicate_using_set(nums1))