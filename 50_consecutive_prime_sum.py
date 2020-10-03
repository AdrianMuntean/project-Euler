import math


def sieve(n):
    primes = {i: True for i in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):
        if primes.get(i):
            for x in range(i * i, n, i):
                primes.pop(x, None)

    return primes


def find_largest_consecutive_2(primes, n):
    """
    Iterate over the keys and compute the sum for each one
    """
    largest_count = 0
    largest_sum = 0

    keys = list(primes.keys())
    for k in range(0, len(keys)):
        sum = keys[k]
        count = 1

        for x in range(k + 1, len(keys)):
            if keys[x] + sum > n:
                break

            sum += keys[x]
            count += 1

            if count > largest_count and primes.get(sum):
                largest_sum = sum
                largest_count = count

    return largest_sum


def consecutive_prime_sum(n):
    primes = sieve(n)
    return find_largest_consecutive_2(primes, n)


print(consecutive_prime_sum(1000000))  # 997651
