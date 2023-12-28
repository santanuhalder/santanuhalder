def maxArea(height: list) -> int:
    max = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            if min(height[j], height[i]) * abs(j - i) > max:
                max = min(height[j], height[i]) * abs(j - i)
    return max

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))


