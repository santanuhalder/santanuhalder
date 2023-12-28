def gcd(n1, n2):
	if n1 == 0:
		return n2
	elif n2 == 0:
		return n1
	if n1 > n2:
		return gcd(n2, n1 % n2)
	else:
		return gcd(n1, n2 % n1)


def gcd_optimized(n1, n2):
	if n2 == 0:
		return n1
	return gcd_optimized(n2, n1 % n2)

# n1 = 18
# n2 = 12
#
# n3 = 25
# n4 = 15
#
# n5 = 40
# n6 = 60
#
# print(gcd(n1, n2))
# print(gcd(n3, n4))
# print(gcd(n5, n6))

# print(gcd_optimized(n1, n2))
# print(gcd_optimized(n3, n4))
# print(gcd_optimized(n5, n6))

arr1 = [2, 5, 6, 9, 10]
arr1.sort()

arr2 = [7,5,6,8,3]
arr2.sort()

arr3 = [3,3]
arr3.sort()


print(gcd(arr1[0], arr1[-1]))
print(gcd(arr2[0], arr2[-1]))
print(gcd(arr3[0], arr3[-1]))







