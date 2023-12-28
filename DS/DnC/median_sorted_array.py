def median_of_sorted_array(numsx, numsy):
	if len(numsx) > len(numsy):
		return median_of_sorted_array(numsy, numsx)

	lenx = len(numsx)
	leny = len(numsy)
	low = 0
	high = lenx

	while high >= low:
		partitionx = (low + high) // 2
		partitiony = (lenx + leny + 1) // 2 - partitionx

		max_left_x = -float('inf') if partitionx == 0 else numsx[partitionx - 1]
		min_right_x = float('inf') if partitionx == lenx else numsx[partitionx]

		max_left_y = -float('inf') if partitiony == 0 else numsy[partitiony - 1]
		min_right_y = float('inf') if partitiony == leny else numsy[partitiony]

		if max_left_x <= min_right_y and max_left_y <= min_right_x:
			if (lenx + leny) % 2 == 0:
				return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
			else:
				return max(max_left_x, max_left_y)
		elif max_left_x > min_right_y:
			high = partitionx - 1
		else:
			low = partitionx + 1


arrx1 = [1, 3, 5]
arry1 = [2, 4, 6]

arrx2 = [1, 1, 1]
arry2 = [2, 2, 2]

arrx3 = [2, 3, 5, 8]
arry3 = [1, 4, 6, 7, 9]

arrx4 = [10, 15, 20, 25, 30, 35]
arry4 = [40, 45]


print(median_of_sorted_array(arrx1, arry1))
print(median_of_sorted_array(arrx2, arry2))
print(median_of_sorted_array(arrx3, arry3))
print(median_of_sorted_array(arrx4, arry4))

