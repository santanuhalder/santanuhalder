def inter(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    s = set1.intersection(set2)
    return s


numbers1 = [1, 2, 2, 1]
numbers2 = [2, 2]

# numbers1 = [4,9,5]
# numbers2 = [9,4,9,8,4]
print(inter(numbers1, numbers2))