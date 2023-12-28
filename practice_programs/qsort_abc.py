def qsort(input_list: list):
    if len(input_list) < 2:
        return input_list
    else:
        pivot_index = len(input_list) // 2
        lower = [i for i in input_list[0 : pivot_index] if i <= input_list[pivot_index]] + \
                [i for i in input_list[pivot_index + 1:] if i <= input_list[pivot_index]]

        higher = [i for i in input_list[0 : pivot_index] if i >= input_list[pivot_index]] + \
                [i for i in input_list[pivot_index + 1:] if i >= input_list[pivot_index]]

    return qsort(lower) + [input_list[pivot_index]] + qsort(higher)


l = [1,2,34, 5, 9, 0, -1]
print(qsort(l))