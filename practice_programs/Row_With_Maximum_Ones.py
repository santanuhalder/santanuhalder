def count_ones(mat):
    maxCount = 0
    res = list()

    for i in range(len(mat)):
        countDict = dict()
        for j in range(len(mat[i])):
            countDict[mat[i][j]] = countDict.setdefault(mat[i][j], 0) + 1
        try:
            if countDict[1] > maxCount:
                res.clear()
                maxCount = countDict[1]
                res.extend([i, maxCount])
        except:
            pass
    return res


input = [[1, 0, 1], [0, 0, 1], [1, 1, 0]]
print(count_ones(input))


