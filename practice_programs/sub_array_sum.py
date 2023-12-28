def subArray(arr, s):
    A, X = [], []
    current_sum = 0
    start = 0
    sumFound = False

    for i in range(len(arr)):
        current_sum = current_sum + arr[i]
        A.append(i + 1)

        while current_sum > s:
            current_sum = current_sum - arr[start]
            A.pop(0)
            start += 1
        if current_sum == s:
            sumFound = True
            break

    if sumFound:
        X = [A[0], A[len(A) - 1]]
    else:
        X.append(-1)
    return X

arr = [1,2,3,4]
# arr = [1-1,2-2,3-3,4-4,5-5,6-6,7-7,8-8,9-9,10-10]
sum = 0
print(subArray(arr, sum))



