def min_subarray(arr, target):
    l, total = 0, 0
    res = float("inf")
    ind = []
    last_item_popped = 0

    for r in range(len(arr)):
        total += arr[r]
        ind.append(r)
        while total >= target:
            res = min(res, r - l + 1)
            last_item_popped = ind[0]
            ind.pop(0)
            total -= arr[l]
            l += 1
    if res != float("inf") and len(ind) == 0:
        ind.append(last_item_popped)
    elif res != float("inf") and len(ind) > 0:
        ind.insert(0, last_item_popped)
    print("ind array {}".format(ind))
    return 0 if res == float("inf") else res


target_ = 7
arr_ = [2, 3, 1, 2, 4, 3]

# arr_ = [1, 4, 4]
# target_ = 4
print(min_subarray(arr_, target_))

