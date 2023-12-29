"""
Given a string s, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u',
and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s= "hello"
Output: "holle"

Example 2:
Input: s= "AEIOU"
Output: "UOIEA"

Example 3:
Input: s= "DesignGUrus"
Output: "DusUgnGires"
"""
def reverse_vowels(txt):
	vowel = 'aeiouAEIOU'
	vowel_set = set(vowel)
	low, high = 0, len(txt) - 1
	input = list(txt)

	while high > low:
		while low < high and input[low] not in vowel_set:
			low += 1
		while low < high and input[high] not in vowel_set:
			high -= 1
		input[low], input[high] = input[high], input[low]
		low += 1
		high -= 1
	return ''.join(input)


str1 = "hello"
str2 = "AEIOU"
str3 = "DesignGUrus"

print(reverse_vowels(str1))
print(reverse_vowels(str2))
print(reverse_vowels(str3))
