set_a = {"Santanu", "Praveen", "Vish", "Raj"}

set_b = {"Santanu", "Vish", "Raj"}

x = set_a.union(set_b)

print(set_a.intersection(set_b))
print(set_a.isdisjoint(set_b))

set_a.update(set_b)

print(set_a)


