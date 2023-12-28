"""
Given a collection of pairs where each pair contains two elements [a, b],
find the maximum length of a chain you can form using pairs.
A pair [a, b] can follow another pair [c, d] in the chain if b < c.
You can select pairs in any order and don't need to use all the given pairs.
"""
def pair_chain(nums):
	nums.sort(key=lambda x: x[1])
	chain_count = 0
	current_end = -float('inf')

	for num in nums:
		if num[0] > current_end:
			chain_count += 1
			current_end = num[1]
	return chain_count


input_arr1 = [[1, 2], [3, 4], [2, 3]]
input_arr2 = [[5, 6], [1, 2], [8, 9], [2, 3]]
input_arr3 = [[7, 8], [5, 6], [1, 2], [3, 5], [4, 5], [2, 3]]
print(pair_chain(input_arr1))
print(pair_chain(input_arr2))
print(pair_chain(input_arr3))
