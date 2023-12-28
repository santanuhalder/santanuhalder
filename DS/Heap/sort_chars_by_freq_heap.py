import heapq
from collections import Counter


def sort_by_freq_heap(s):
	freq = Counter(s)
	max_heap = [(-v, k) for k, v in freq.items()]
	heapq.heapify(max_heap)
	res = ""

	while max_heap:
		occurences, char = heapq.heappop(max_heap)
		res += char*(-occurences)
	return res

s1 = "tree"
s2 = "cccaaa"
s3 = "Aabb"
s4 = "tee"
s5 = "loveleetcode"

print(sort_by_freq_heap(s1))
print(sort_by_freq_heap(s2))
print(sort_by_freq_heap(s3))
print(sort_by_freq_heap(s4))
print(sort_by_freq_heap(s5))

