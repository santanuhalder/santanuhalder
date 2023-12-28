nums = [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]

space = 0
max_space = 0

for i in range(len(nums)):
    if nums[i] == 0:
        space += 1
    elif nums[i] == 1:
        space = 0
    if space > max_space:
        max_space = space

print(max_space)