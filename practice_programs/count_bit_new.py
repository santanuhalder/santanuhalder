bit_number = 0b00101
count = 0

while bit_number != 0:
    if bit_number & 1 == 1:
        count += 1
    bit_number = bit_number >> 1

print(count)