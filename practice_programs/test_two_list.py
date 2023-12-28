input1 = [2, 4, 90, 99, 100]
input2 = [1, 3, 6, 7, 100, 120, 150]


i, j = 0, 0
len1 = len(input1)
len2 = len(input2)
merged = []

while i < len1 and j <len2:
    if input1[i] < input2[j]:
        merged.append(input1[i])
        i +=1
    else:
        merged.append(input2[j])
        j +=1

merged = merged + input2[j+1:]

print(merged)



