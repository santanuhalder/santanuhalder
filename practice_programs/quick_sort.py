def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = len(arr) // 2
        lower = [i for i in arr[0:pivot_index] if i <= arr[pivot_index]] + [i for i in arr[pivot_index + 1:] if i <= arr[pivot_index]]
        higher = [i for i in arr[0:pivot_index] if i >= arr[pivot_index]] + [i for i in arr[pivot_index + 1:] if i >= arr[pivot_index]]
        return qsort(lower) + [arr[pivot_index]] + qsort(higher)


number_arr = [10, 5, 2, 3, 1, 0, 90, 50]
print(qsort(number_arr))



