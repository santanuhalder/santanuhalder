def merge(left_array: list, right_array: list) -> list:
    i = j = k = 0
    res = list()
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
             res.append(left_array[i])
             i += 1
        else:
            res.append(right_array[j])
            j += 1
    res = res + left_array[i:] + right_array[j:]
    return res

def merge_sort(nums: list):
    if len(nums) < 2:
        return  nums
    mid = len(nums) //2
    left = merge_sort(nums[:mid])

    right = merge_sort(nums[mid:])

    print(left)
    print(right)

    return merge(left, right)


nums1 = [1, 2, 4, 7, 9]
nums2 = [-1, 3, 5, 19, 20]
nums3 = [20, 2, 6, 10, 4, -1, 37, 1, 4, 20]

print(merge_sort(nums3))



