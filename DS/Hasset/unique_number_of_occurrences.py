def unique_occurences(arr):
	freq = {}
	for num in arr:
		freq[num] = freq.setdefault(num, 0) + 1
	return len(freq) == len(set(freq.values()))

input_nums1 = [4, 5, 4, 6, 6, 6]
input_nums2 = [7, 8, 8, 9, 9, 9, 10, 10]
input_nums3 = [11, 12, 13, 14, 14, 15, 15, 15]

print(unique_occurences(input_nums1))
print(unique_occurences(input_nums2))
print(unique_occurences(input_nums3))
