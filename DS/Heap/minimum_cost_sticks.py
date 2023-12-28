import heapq


def connectSticks(sticks):
	heapq.heapify(sticks)
	min_cost = 0

	while len(sticks) >= 2:
		running_cost = 0
		running_cost += heapq.heappop(sticks)
		running_cost += heapq.heappop(sticks)
		heapq.heappush(sticks, running_cost)
		min_cost += running_cost
	return min_cost


input_arr1 = [2, 4, 3]
input_arr2 = [1, 8, 2, 5]
input_arr3 = [5, 5, 5, 5]
print(connectSticks(input_arr1))
print(connectSticks(input_arr2))
print(connectSticks(input_arr3))


