def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2

	l_array = merge_sort(arr[:mid])
	r_array = merge_sort(arr[mid:])

	return merge(l_array, r_array)

def merge(left_array, right_array):
	i, j = 0, 0
	result = list()

	while i < len(left_array) and j < len(right_array):
		if left_array[i] < right_array[j]:
			result.append(left_array[i])
			i += 1
		else:
			result.append(right_array[j])
			j += 1
	return result + left_array[i:] + right_array[j:]


arr1 = [5, 2, 8, 3, 1, 6]
print(merge_sort(arr1))

arr2 = [-5, 2, -8, 3, 100, 1, 6, 200, 0]
print(merge_sort(arr2))


