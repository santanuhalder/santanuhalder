def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) - 1]
	left, middle, right = list(), list(), list()

	for num in arr:
		if num < pivot:
			left.append(num)
		elif num == pivot:
			middle.append(num)
		else:
			right.append(num)
	return quick_sort(left) + middle + quick_sort(right)

arr1 = [5, 2, 8, 3, 1, 6]
print(quick_sort(arr1))

arr2 = [-5, 2, -8, 3, 100, 1, 6, -300, 0]
print(quick_sort(arr2))