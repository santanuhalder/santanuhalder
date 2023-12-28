def reverseWords(txt):
    l = txt.split(" ")
    l.reverse()
    return " ".join(l)


def reverse_word(txt):
    x = txt.split()
    return " ".join(x[::-1])

input_string = "Hello World!"
print(reverseWords(input_string))
print(reverse_word(input_string))