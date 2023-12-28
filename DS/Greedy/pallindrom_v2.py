def is_pallindrome(txt, l, r):
    while r > l:
        if txt[r] != txt[l]:
            return False
        r -= 1
        l += 1
    return True


def pallindrome_v2(s):
    left, right = 0, len(s) - 1
    while right > left:
        if s[left] != s[right]:
            return is_pallindrome(s, left + 1, right) or is_pallindrome(s, left, right - 1)
        right -= 1
        left += 1
    return True


input_txt1 = "racecar"
input_txt2 = "abccdba"
input_txt3 = "abcdef"

print(pallindrome_v2(input_txt1))
print(pallindrome_v2(input_txt2))
print(pallindrome_v2(input_txt3))