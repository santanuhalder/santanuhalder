# Given an array, print the Next Greater Element (NGE) for every element.
# The Next Greater Element for an element x is the first greater element on the right side of x in the array.
# Elements for which no greater element exist, consider the next greater element as -1.

def next_greater_element(nums):
    res = list()

    for i in range(len(nums)):
        is_greater_found = False
        greater_element = None
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                greater_element = nums[j]
                is_greater_found = True
                break
        if is_greater_found:
            res.append(greater_element)
        else:
            res.append(-1)
    return res
# res 12
# stack 12

def next_greater_by_stack(arr):
    res = []*len(arr)
    stack = []*len(arr)

    for i in range(len(arr) -1, -1, -1):
        while stack and stack[-1] < arr[i]:
            stack.pop()
        if not stack:
            res.append(-1)
            stack.append(arr[i])
        else:
            res.append(stack[-1])
            stack.append(arr[i])



    res.reverse()
    return res


input= [13, 7, 6, 12]
#print(next_greater_element(Input))
print(next_greater_by_stack(input))

