def diagonalSum(mat):
    total_sum = 0
    for i in range(len(mat)):
        # total_sum += mat[i][i] + mat[i][~i] # or total_sum += mat[i][i] + mat[i][len(mat) - i - 1]
        total_sum += mat[i][i] + mat[i][len(mat) - i - 1]

    if len(mat) % 2 == 1:
        mid = len(mat) // 2
        total_sum -= mat[mid][mid]
    return total_sum


matrix = [[4, 6, 9, 0],
          [5, 4, 8, 3],
          [7, 8, 9, 1],
          [0, 7, 8, 5]]

print(diagonalSum(matrix))