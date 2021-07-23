"""
Since we know that we need to search near 3/7 we can define the search range from 0.4285714 to 3/7. 
1. The solution is not 100% generic, since it has the range selectors tailored to search near 3/7. Could be extended to be a generic solution
2. It computes in around 14 seconds
"""
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
    skipped = 0
    fraction = a[0] / a[1]
    reduced_proper_fractions = []
    for d in range(1, upper_limit + 1):
        n_start = int(0.4285714 * d)
        n_end = int(fraction * d)
        if n_start == 0:
            continue
        for n in range(n_start, n_end + 1):
            div = n / d
            if div >= fraction:
                skipped += 1
                continue

            if prime_btw_them(n, d):
                reduced_proper_fractions.append((n, d))
    print(f"{skipped} skipped")
    return reduced_proper_fractions


def just_before(a, d):
    fractions = order_fraction(a, d)
    fractions.sort(key=lambda x: x[0] / x[1])
    last_one = fractions[-1]
    return last_one[0]


# print(just_before((3, 7), 10 ** 2))
print(just_before((3, 7), 10 ** 6))  # 428570
