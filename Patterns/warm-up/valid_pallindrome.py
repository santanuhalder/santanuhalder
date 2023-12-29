"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: sentence = "A man, a plan, a canal, Panama!"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: sentence = "Was it a car or a cat I saw?"
Output: true
Explanation: Explanation: "wasitacaroracatisaw" is a palindrome.
"""

def pallindrome(txt):
	low, high = 0, len(txt) - 1

	while high > low:
		while high > low and not txt[low].isalpha():
			low += 1
		while high > low and not txt[high].isalpha():
			high -= 1
		if txt[low].casefold() != txt[high].casefold():
			return False
		low += 1
		high -= 1
	return True


sentence1 = "A man, a plan, a canal, Panama!"
sentence2 = "Was it a car or a cat I saw?"
sentence3 = "Was it a car or a cat I saw last night?"

print(pallindrome(sentence1))
print(pallindrome(sentence2))
print(pallindrome(sentence3))