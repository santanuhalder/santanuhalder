class Solution:
    def isValid(self, s):
        d = {')': '(', ']': '[', '}': '{'}
        working_list = list()
        is_valid_bracket = True

        for b in s:
            if b not in d.keys():
                working_list.append(b)
            else:
                if len(working_list) > 0:
                    if d[b] != working_list.pop():
                        is_valid_bracket = False
                else:
                    is_valid_bracket = False

        if len(working_list) > 0:
            is_valid_bracket = False
        return is_valid_bracket


m = Solution()
print(m.isValid("]["))