import math

cache = {}


def sieve(n):
    primes = {i: True for i in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):
        if primes.get(i):
            for x in range(i * i, n, i):
                primes.pop(x, None)

    return primes


def get_factors(n, primes):
    factors = {}
    i = 2
    m = n
    if primes.get(n):
        factors[m] = 1
    else:
        while i <= m / 2:
            if cache.get(n):
                cached_value = cache[n]
                for k, v in cached_value.items():
                    if k in factors:
                        factors[k] = factors[k] + v
                    else:
                        factors[k] = v
                break
            if n % i == 0:
                f = factors.get(i, 0)
                f += 1
                factors[i] = f
                n //= i
            else:
                i += 1
    cache[m] = factors
    return factors


def phi(n, primes):
    factors = get_factors(n, primes)
    p = 1
    for k, v in factors.items():
        p *= k ** (v - 1) * (k - 1)

    return p


def is_permutation(n, m):
    str_n = str(n)
    str_m = str(m)
    sorted_n = sorted(str_n)
    sorted_m = sorted(str_m)

    return sorted_m == sorted_n


def get_totient_min(n, primes):
    smallest = 10 ** 5  # just a large number
    smallest_number = 0
    for i in range(2, n + 1):
        p = phi(i, primes)
        if not is_permutation(i, p):
            continue
        if smallest > (i / p):
            smallest = i / p
            smallest_number = i
    return smallest_number


def totient_min(n):
    """
    1. Basically, re-use lots of problem #69
    2. Just add a check for permutation

    runs in 134.50s, which is a bit slow, but works for now
    """
    primes = sieve(n)
    return get_totient_min(n, primes)


print(totient_min(10 ** 7))  # 8319823