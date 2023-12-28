def is_palondrome(txt: str)-> bool:
    l, r = 0, len(txt) - 1

    while r >=l:
        if txt[l] != txt[r]:
            return False
        r -= 1
        l += 1
    return True


t  = "abxba"
print(is_palondrome(t))