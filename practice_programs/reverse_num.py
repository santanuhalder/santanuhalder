class Solution:
    def reverse(self, x: int) -> int:
        input_number = 0
        if x < 0:
            input_number = x * -1
        else:
            input_number = x
        num = list(str(input_number))
        reversed_num_list = num[::-1]
        reversed_num = int("".join(reversed_num_list))
        if x < 0:
            reversed_num = reversed_num * -1
        return reversed_num


s = Solution()
number = 1534236469
reversed_number = int(s.reverse(number))
print(reversed_number)

print(int(str(number)[::-1]))
