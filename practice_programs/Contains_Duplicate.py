def containsDuplicate(nums):
    if len(nums) == 0:
        return False
    d = dict()
    for val in nums:
        d[val] = d.setdefault(val, 0) + 1
    return True if max(d.values()) > 1 else False


print(containsDuplicate([1, 90, 45, 5, 3]))

