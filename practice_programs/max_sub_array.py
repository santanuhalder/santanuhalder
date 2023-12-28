# sliding window
arr = [1, 5, 5, 3, 40, 7, 16, 4, 9, 12]             # Input array
k = 3                                               # window size
i, j = 0, 0
sum = arr[0]

# Get indices for the window
while j - i + 1 < k:
    j += 1
    sum += arr[j]


maxSum = 0
for m in range(j + 1, len(arr)):
    sum = sum + arr[m] - arr[i]
    #m += 1
    i += 1
    maxSum = max(sum, maxSum)

print(maxSum)
