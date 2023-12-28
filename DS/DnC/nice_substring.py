class Solution:
    @staticmethod
    def findLongestNiceSubstring(s):
        if s is None or len(s) <= 1:
            return ""  # Base condition

        # Check if the whole string is a nice substring
        if Solution.isNice(s):
            return s

        longest = ""

        # Divide and conquer: Check for each split point
        for i in range(len(s)):
            left = s[:i]
            right = s[i + 1:]

            # Recursively find the longest nice substring in the left and right parts
            left_nice = Solution.findLongestNiceSubstring(left)
            right_nice = Solution.findLongestNiceSubstring(right)

            # Conquer: Choose the longer one between left_nice and right_nice
            if len(left_nice) >= len(right_nice):
                if len(left_nice) > len(longest):
                    longest = left_nice
            else:
                if len(right_nice) > len(longest):
                    longest = right_nice

        return longest

    # Helper method to check if a string is a nice substring
    @staticmethod
    def isNice(s):
        char_map = [0] * 128  # ASCII character set size
        for c in s:
            char_map[ord(c)] += 1

        for c in s:
            # Check both cases for each character
            if (c.islower() and char_map[ord(c.upper())] == 0) or (c.isupper() and char_map[ord(c.lower())] == 0):
                return False
        return True

# Testing the algorithm with example inputs
print(Solution.findLongestNiceSubstring("BbCcXxY"))  # Expected: BbCcXx
print(Solution.findLongestNiceSubstring("aZAbcD"))   # Expected: (empty string)
print(Solution.findLongestNiceSubstring("qQwWeErR")) # Expected: qQwWeErR
