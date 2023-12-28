def number_freq(arr, key):
	return calculate_freq(arr, key, 0)


def calculate_freq(arr, key, index):
	if index == len(arr):
		return 0

	count = 1 if arr[index] == key else 0
	return count + calculate_freq(arr, key, index + 1)

arr1 = [2, 4, 6, 8, 4]
key1 = 4
arr2 = [1, 3, 5, 7, 9]
key2 = 2
arr3 = [1, 2, 2, 2, 3]
key3 = 2

print(number_freq(arr1, key1))
print(number_freq(arr2, key2))
print(number_freq(arr3, key3))




