def rem_dup(nums: list) -> list:
    res = list()
    res.append(nums[0])
    i, j = 0, 0
    while i < len(nums):
        if res[j] != nums[i]:
            res.append(nums[i])
            j += 1
            i += 1
        else:
            i += 1
    return res


numbers = [1, 1, 7, 8, 9, 9, 10]
print(rem_dup(numbers))
