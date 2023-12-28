class Solution:
	def findMajority(self, arr):
		freq = dict()
		for num in arr:
			freq[num] = freq.setdefault(num, 0) + 1
		max_element = max(freq, key=freq.get)
		return max_element


	def majority(self, arr):
		freq = {num: arr.count(num) for num in arr}

		max_element = max(freq, key=freq.get)
		return max_element


solution = Solution()
input_nums1 = [1, 2, 2, 3, 2]
print(solution.findMajority(input_nums1))