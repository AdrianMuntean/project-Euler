import string
from itertools import *
import math


def is_prime(n, primes):
    prime = primes.get(n)
    if prime:
        return True

    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def sieve(n):
    primes = {i: True for i in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):
        if primes.get(i):
            for x in range(i * i, n, i):
                primes.pop(x, None)

    return primes


def all_primes(pair, primes):
    for p in permutations(pair, 2):
        combined_number = int(str(f'{p[0]}{p[1]}'))
        if not is_prime(combined_number, primes):
            return False

    return True


def prime_pair_set():
    # Compute the primes up to 10^4
    primes = sieve(10**4)
    primes_pairs = combinations(primes.keys(), 4)
    for pair in primes_pairs:
        if all_primes(pair, primes):
            return pair

# 1st iteration: brute force. Taking too long and is kind of dumb
print(prime_pair_set())
