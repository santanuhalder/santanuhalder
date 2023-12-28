def removeElement(nums: list, val: int) -> int:
    i = 0
    count = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            count += 1
        else:
            i = i + 1
    return nums

numbers = [0,1,2,2,3,0,4,2,2]
print(removeElement(numbers, 0))