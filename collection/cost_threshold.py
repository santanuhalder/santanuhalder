def calculate_top_x_members(members, cost_threshold_percent):
    l, total = 0, 0
    res = float("inf")
    ind = []
    last_item_popped = 0

    for r in range(len(members)):
        total += members[r]
        ind.append(r)
        while total >= cost_threshold_percent:
            res = min(res, r - l + 1)
            last_item_popped = ind[0]
            ind.pop(0)
            total -= members[l]
            l += 1
    if res != float("inf") and len(ind) == 0:
        ind.append(last_item_popped)
    elif res != float("inf") and len(ind) > 0:
        ind.insert(0, last_item_popped)
    print("ind array {}".format(ind))
    return [] if res == float("inf") else ind


threshold = 7
members = {"John": 2, "Brad": 3, "Alice": 1, "Peter": 2, "Donald": 4, "Fred": 3}
member_array = []
cost_array = []

for key, val in members.items():
    member_array.append(key)
    cost_array.append(val)

# arr_ = [1, 4, 4]
# target_ = 4
members_ = calculate_top_x_members(cost_array, threshold)
print("Members making the cost threshold are below ")

for i in range(len(members_)):
    print("{}".format(member_array[members_[i]]))

