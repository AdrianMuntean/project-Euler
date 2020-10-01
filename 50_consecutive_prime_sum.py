import math


def sieve(n):
    primes = {i: True for i in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):
        if primes.get(i):
            for x in range(i * i, n, i):
                primes.pop(x, None)

    return primes


def find_largest_consecutive(primes):
    largest = 0
    largest_prime = 0
    for k in primes.keys():
        for k2 in primes.keys():
            diff = k
            largest_for_this = 0
            for k3 in primes.keys():
                if k2 > k3:
                    continue

                diff = diff - k3
                largest_for_this += 1

                if diff <= 0:
                    break

            if diff == 0 and largest_for_this > largest:
                largest = largest_for_this
                largest_prime = k

    return largest_prime


def consecutive_prime_sum(n):
    primes = sieve(n)
    return find_largest_consecutive(primes)


print(consecutive_prime_sum(1000))
