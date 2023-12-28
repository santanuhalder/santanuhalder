def counting_elements(arr):
	s = set(arr)
	count = 0
	for ele in arr:
		if (ele + 1) in s:
			count += 1
	return count

input_arr1 = [4, 3, 1, 5, 6]
input_arr2 = [7, 8, 9, 10]
input_arr3 = [11, 13, 15, 16]
print(counting_elements(input_arr1))
print(counting_elements(input_arr2))
print(counting_elements(input_arr3))


