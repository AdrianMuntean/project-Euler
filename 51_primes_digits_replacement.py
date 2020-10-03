import math
import itertools


def sieve(n):
    primes = {i: True for i in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):
        if primes.get(i):
            for x in range(i * i, n, i):
                primes.pop(x, None)

    return primes


def count_prime_variations(number, no_digits, digit_value, primes):
    if no_digits == 0:
        return 0
    max_count = 0
    for i in range(0, len(str(number)) - 1):
        str_number = list(str(number))
        str_number[i] = str(digit_value)
        variation = int(''.join(str_number))
        if primes.get(variation):
            max_count += 1
        
    return max_count


def variations(number, primes):
    max_count = 0
    for i in range(1, len(str(number))):
        for j in range(1, 10):
            count = count_prime_variations(number, i, j, primes)
            if count > max_count:
                max_count = count
    return count



def consecutive_prime_sum(family_numbers):
    primes = sieve(10**6)
    for i in primes.keys():
        if i < 10:
            continue
        primes_count = variations(i, primes)
        if primes_count == family_numbers:
            return i


print(consecutive_prime_sum(6))
