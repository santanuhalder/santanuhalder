# Binary search program
# this method takes a sorted array
# https://www.geeksforgeeks.org/python-program-for-binary-search/

def binary_search(arr, low, high, x): # this method takes a sorted array (arr), low and high indices and
    # number x to search
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return "The number {0} is not present in the array {1}".format(x, arr)

arr_orig = [2, 5, 10, 20, 30]
print(binary_search(arr_orig, 0, 4, 78))
