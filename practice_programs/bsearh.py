def bin_search(nums: list, low, high, key: int) -> int:
    if high >= low:
        mid = (high + low) // 2

        if nums[mid] == key:
            return mid
        elif nums[mid] > key:
            return bin_search(nums, low, mid - 1, key)
        else:
            return bin_search(nums, mid + 1, high, key)

    else:
        return -1


numbers = [1, 2, 3, 4, 6, 7, 90, 99, 100, 100, 150]
print(bin_search(numbers, 0, len(numbers) - 1, 150))




