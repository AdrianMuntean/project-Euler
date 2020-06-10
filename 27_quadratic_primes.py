import math


def is_prime(number):
    d = 2
    while d < math.sqrt(abs(number)):
        if number % d == 0:
            return False
        d += 1

    return True


def no_consecutive_primes(a, b):
    no_primes = 0
    n = 0
    while True:
        if not is_prime(n ** 2 + a * n + b):
            return no_primes
        n += 1
        no_primes += 1


def quadratic_primes(r):
    longest_no_primes = 0
    product = 0
    for a in range(-r + 1, r):
        for b in range(-r, r + 1):
            no = no_consecutive_primes(a, b)
            if longest_no_primes < no:
                longest_no_primes = no
                product = a * b
    return product


print(quadratic_primes(1000))  # -59231
