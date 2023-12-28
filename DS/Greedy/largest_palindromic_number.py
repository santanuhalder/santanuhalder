class Solution:
	def largestPalindromic(self, num: str) -> str:
		freq = [0]*10
		for n in num:
			freq[int(n)] += 1
		middle = ''
		first_half = ''

		for i in range(9, -1, -1):
			if freq[i] % 2 == 0:
				first_half += str(i)*(int(freq[i] // 2))
			elif freq[i] > 1:
				first_half += str(i)*(int((freq[i] - 1) // 2))
				if not middle:
					middle += str(i)
			else:
				if not middle:
					middle += str(i)

		if not first_half:
			return middle if middle else '0'
		elif all(d == '0' for d in first_half):
			return middle if middle else '0'

		return first_half + middle + first_half[::-1]




numbers1 = "323211444"
numbers2 = "987789"
numbers3 = "54321"
numbers4 = "00009"

solution = Solution()
# print(solution.largestPalindromic(numbers1))
# print(solution.largestPalindromic(numbers2))
# print(solution.largestPalindromic(numbers3))
print(solution.largestPalindromic(numbers4))