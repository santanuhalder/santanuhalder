class Solution:
    def isIsomorphic(s: str, t: str) -> bool:
        first_word = dict()
        second_word = dict()
        i = j = 1
        if len(s) != len(t):
            return False

        first_word[0] = s[0]
        second_word[0] = t[0]
        while i < len(s) and j < len(t):
            pass
            
