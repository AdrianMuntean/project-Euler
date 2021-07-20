import math

factors_of = {}


def get_factors(n):
    if factors_of.get(n):
        return factors_of.get(n)
    factors = [1]
    if n > 1:
        factors.append(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(n // i)

    factors_of[n] = factors
    return factors


def prime_btw_them(n, d):
    factors = get_factors(n)
    array = [1 for x in factors if d % x == 0]

    return sum(array) == 1


def order_fraction(a, upper_limit):
    fraction = a[0] / a[1]
    reduced_proper_fractions = []
    for d in range(1, upper_limit + 1):
        for n in range(1, d):
            if n / d >= fraction:
                continue
            if prime_btw_them(n, d):
                reduced_proper_fractions.append((n, d))
                if d % 10000 == 0:
                    print(n, d)
    return reduced_proper_fractions


def just_before(a, d):
    fractions = order_fraction(a, d)
    fractions.sort(key=lambda x: x[0] / x[1])
    return fractions[-1][0]


print(just_before((3, 7), 10 ** 6))
# print(just_before((3, 7), 8))
