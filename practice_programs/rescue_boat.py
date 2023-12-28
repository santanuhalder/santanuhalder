def rescue_boat(arr: list, limit: int) -> int:
	"""
	We are given an array people where each element people[i] represents the weight of the i-th person.
	There is also a weight limit for each boat. Each boat can carry at most two people at a time, but the combined
	weight of these two people must not exceed limit. The objective is to determine the minimum number of boats
	required to carry all the people.
	Example
	Input: people = [10, 55, 70, 20, 90, 85], limit = 100
	Output: 4
	:param arr:
	:param limit:
	:return:
	"""
	arr.sort() # sorting the list
	# take two pointers - one at the beginning and one at the end
	left, right = 0, len(arr) - 1
	num_of_boats = 0

	while right > left:
		if arr[left] + arr[right] <= limit:
			left += 1
			right -= 1
			num_of_boats += 1
		else:
			right -= 1
			num_of_boats += 1
	if right == left:
		num_of_boats += 1
	return num_of_boats


people = [10, 55, 70, 20, 90, 85]
limit = 100
print(rescue_boat(people, limit))



