class ReverseString:
    def reverse_str(self, input_string):
        return input_string[::-1]

    def reverse(self, input_string):
        l = list()
        res = list()
        for i in input_string:
            l.append(i)
        for i in range(len(l)):
            res.append(l.pop())
        return "".join(res)

    def string_reversal(self, input_string):
        l = list(input_string)
        reversed_str = ""
        while l:
            reversed_str += l.pop()
        return reversed_str

c = ReverseString()
str = "Hello, World!"
print(c.reverse_str(str))
print(c.reverse(str))
print(c.string_reversal(str))

