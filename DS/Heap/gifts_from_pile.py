import heapq


def take_gifts(gifts, k):
	max_heap = [-gift for gift in gifts]
	heapq.heapify(max_heap)

	for _ in range(k):
		current_element = -heapq.heappop(max_heap)
		heapq.heappush(max_heap, -int(current_element**0.5))
	return -sum(max_heap)


gifts1 = [4, 9, 16]
k1 = 2

gifts2 = [1, 2, 3]
k2 = 1

gifts3 = [25, 36, 49]
k3 = 3

print(take_gifts(gifts1, k1))
print(take_gifts(gifts2, k2))
print(take_gifts(gifts3, k3))