from collections import Counter

def isanagram1(s1, s2):
    if Counter(s1) == Counter(s2):
        return True
    else:
        return False

def isanagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

def test_anagram(s1, s2):
    if set(s1) == set(s2):
        return True
    else:
        return False


str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"

x = test_anagram(str1, str2)
if x == False:
    print("Two strings '{}' and '{}' are not anagram".format(str1, str2))
if x == True:
    print("Two strings '{}' and '{}' are  anagram".format(str1, str2))