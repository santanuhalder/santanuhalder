def arrayinversion(arr):
    inversion = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversion += 1
    return inversion


arr= [2, 4, 1, 3, 5]
print(arrayinversion(arr))