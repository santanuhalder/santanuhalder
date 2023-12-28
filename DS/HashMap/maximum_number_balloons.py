def max_number_baloons(text):
	freq = {}
	for char in text:
		freq[char] = freq.setdefault(char, 0) + 1
	l = list(freq.values())
	if len(l) < 5:
		return 0
	return min(l)

input_txt1 = "balloonballoon"
input_txt2 = "bbaall"
input_txt3 = "balloonballoooon"
print(max_number_baloons(input_txt1))
print(max_number_baloons(input_txt2))
print(max_number_baloons(input_txt3))


