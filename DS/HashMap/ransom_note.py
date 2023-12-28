def canConstruct(ransomNote, magazine):
	ransomNote_freq = {}
	magazine_freq = {}

	for char in ransomNote:
		ransomNote_freq[char] = ransomNote_freq.setdefault(char, 0) + 1

	for char in magazine:
		magazine_freq[char] = magazine_freq.setdefault(char, 0) + 1

	for k, v in ransomNote_freq.items():
		try:
			if ransomNote_freq[k] > magazine_freq[k]:
				return False
		except KeyError:
			return False
	return True

ransom_note1 = "hello"
magazine1 = "hellworld"

ransom_note2 = "notes"
magazine2 = "stoned"

ransom_note3 = "apple"
magazine3 = "pale"

print(canConstruct(ransom_note1, magazine1))
print(canConstruct(ransom_note2, magazine2))
print(canConstruct(ransom_note3, magazine3))

