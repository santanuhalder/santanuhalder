class Solution:
	def minMoves(self, nums):
		min_distance = 0
		max_index_left = nums.index(max(nums)) + 1
		max_index_right = len(nums) - max_index_left + 1


		min_index_left = nums.index(min(nums)) + 1
		min_index_right = len(nums) - min_index_left + 1


		from_left = max(max_index_left, min_index_left)
		from_right = max(max_index_right, min_index_right)
		from_both_end = min(max_index_right, min_index_right) + min(max_index_left, min_index_left)

		min_distance = min(from_left, from_right, from_both_end)

		# if from_left < from_right and min_distance > from_left:
		# 	min_distance = from_left
		# elif from_left > from_right and min_distance > from_right:
		# 	min_distance = from_right
		# elif from_right == from_left and min_distance > from_left:
		# 	min_distance = from_right

		return min_distance


input_nums1 = [3, 2, 5, 1, 4]
input_nums2 = [7, 5, 6, 8, 1]
input_nums3 = [2, 4, 10, 1, 3, 5]
input_nums4 = [5, 3, 2, 4, 1]

solution = Solution()
print(solution.minMoves(input_nums1))
print(solution.minMoves(input_nums2))
print(solution.minMoves(input_nums3))
print(solution.minMoves(input_nums4))