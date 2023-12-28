from heapq import *


class Solution:
	def __init__(self):
		self.minHeap = []
		self.maxHeap = []

	def insertNum(self, num):
		if not self.maxHeap or num <= -self.maxHeap[0]:
			heappush(self.maxHeap, -num)
		else:
			heappush(self.minHeap, num)

		if len(self.maxHeap) > len(self.minHeap) + 1:
			heappush(self.minHeap, -heappop(self.maxHeap))
		elif len(self.minHeap) > len(self.maxHeap):
			heappush(self.maxHeap, -heappop(self.minHeap))

	def findMedian(self):
		if len(self.minHeap) == len(self.maxHeap):
			return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
		else:
			return -self.maxHeap[0]



sol = Solution()
input_nums1 = [3, 1, 5, 4]


for i in range(len(input_nums1)):
	sol.insertNum(input_nums1[i])

print(sol.findMedian())





