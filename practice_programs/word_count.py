line = "A dog jumps and catches a big cat"

x = line.split(" ")
indexOfDog = x.index("dog")
indexOfCat = x.index("cat")

print(x)

if indexOfCat > indexOfDog:
    print(indexOfCat - indexOfDog - 1)
else:
    print(indexOfDog - indexOfCat - 1)

