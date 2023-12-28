def reverse_integer(number: int) -> int:
    reverse = 0
    while number != 0:
        reverse = reverse * 10 + number % 10
        number = number // 10
    return reverse


print(reverse_integer(701))

