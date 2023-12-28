def fibo(n: int) -> int:
    """
    :param num:
    :return:
    """
    f1, f2 = 0, 1
    if n <= 1:
        return n

    for i in range(2, n + 1):
        sum = f1 + f2
        f1 = f2
        f2 = sum

    return sum

print(fibo(8))