def count_bit(i: int) -> int:
    count = 0
    while i != 0:
        count += i & 1
        i >>= 1
    return count


bin_number = 0b000000
print(count_bit(bin_number))

