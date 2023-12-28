def bin_search(arr, low, high, key):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == key:
			return "The key {} was found at an index {} of array {}.".format(key, mid, arr)
		if arr[mid] > key:
			return bin_search(arr, low, high - 1, key)
		else:
			return bin_search(arr, low + 1, high, key)

	else:
		return print("The key {} is not present in the input array {}.".format(key, arr))



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
arr3 = [3, 6, 9, 12, 15]
key1 = 4
key2 = 5
key3 = 15

print(bin_search(arr1, 0, len(arr1) - 1, key1))
print(bin_search(arr2, 0, len(arr2) - 1, key2))
print(bin_search(arr3, 0, len(arr3) - 1, key3))