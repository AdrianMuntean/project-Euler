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


def get_totient_max(n, primes):
    largest = 0
    largest_number = 0
    for i in range(2, n + 1):
        p = phi(i, primes)
        if largest < i / p:
            largest = i / p
            largest_number = i
    return largest_number


def totient_max(n):
    """
    1. compute the primes first using the sieve of Eratosthenes, it's really effective
    2. compute phi(n) using the factorization of the number.
    phi(n) = n*(1-1/p1)*(1-1/p2)*...*(1-1/pn) = p1**(k1-1) (p1-1)...pr**(kr-1)(pr - 1)

    runs in 5s
    """
    primes = sieve(n)
    return get_totient_max(n, primes)


print(totient_max(10 ** 6))  # 510510