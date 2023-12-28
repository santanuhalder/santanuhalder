def temp(tmp):
    temp_desc = None
    if tmp > 50:
        temp_desc = "warm"
    else:
        temp_desc = "cold"
    return temp_desc

nums = "0123"
letters = "abcd"

names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

# d = {name: hero for name, hero in zip(names, heroes) if name != "Peter"}
# print(d)

#
# d = {name: hero for name, hero in zip(names, heroes)}
# print(d)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_gen = (i*i for i in nums if i % 2 == 0)

# for i, val in enumerate(my_gen):
#     print(i, val)

temp_in_f = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

temp_in_c = {key: round((5/9)*(val-32)) for key, val in temp_in_f.items() if key != 'Boston'}
# print(temp_in_c)

temp_desc = {key: temp(val) for key, val in temp_in_f.items()}
print(temp_desc)

new_list = [i*i for i in range(1, 11)]

print(new_list)

temp_in_f = [32, 75, 100, 50]

new_temp = [temp(x) for x in temp_in_f]
print(new_temp)

students = [34, 79, 80, 90, 60, 55, 45]
x = list(filter(lambda x: x >= 60, students))
print(x)







