def is_prime(number: int) -> bool:
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    return isPrime


for i in range(1, 21):
    print(i, is_prime(i))

ΩSAQ