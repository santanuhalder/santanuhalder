class Solution:
    def decimalToBinary(self, num):
        res = list()
        output =""
        while num != 0:
            rem = num%2
            res.append(rem)
            num = num//2
        while res:
            output += str(res.pop())
        return output

    def decimalToHex(self, num):
        res = list()
        output =""
        while num != 0:
            rem = num%16
            res.append(rem)
            num = num//16
        while res:
            output += str(res.pop())
        return output

    def decimalToOct(self, num):
        res = list()
        output =""
        while num != 0:
            rem = num%8
            res.append(rem)
            num = num//8
        while res:
            output += str(res.pop())
        return output


r = Solution()
print(r.decimalToBinary(18))
print(r.decimalToHex(222))
print(r.decimalToOct(56))