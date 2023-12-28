def largest_unique_number(A):
	freq = {}
	for num in A:
		freq[num] = freq.setdefault(num, 0) + 1
	max_num = -float('inf')
	for num in A:
		if freq[num] == 1:
			max_num = max(max_num, num)
	return max_num if max_num != -float('inf') else -1


input_arr1 = [5, 7, 3, 7, 5, 8] # Expected Output: 8
input_arr2 = [1, 2, 3, 2, 1, 4, 4] # Expected Output: 3
input_arr3 = [9, 9, 8, 8, 7, 7] # Expected Output: -1

print(largest_unique_number(input_arr1))
print(largest_unique_number(input_arr2))
print(largest_unique_number(input_arr3))
