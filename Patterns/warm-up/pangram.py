def is_pangram(txt):
	chars = dict()
	for char in txt:
		chars[char.lower()] = chars.setdefault(char.lower(), 0) + 1
	return True if len(chars) == 26 else False


sentence1 = "TheQuickBrownFoxJumpsOverTheLazyDog"
sentence2 = "This is not a pangram"
sentence3 = "abcdEfgHijkLmnoPQQQrstUVwxYZ"

print(is_pangram(sentence1))
print(is_pangram(sentence2))
print(is_pangram(sentence3))

