import math


def factorize(number):
    primes = set()
    d = 2
    while number > 1 or d < math.sqrt(number):
        if number % d == 0:
            number /= d
            primes.add(d)
        else:
            d += 1

    return primes


def have_distinct_primes(number, prime_fact):
    prime_set = factorize(number)
    return len(prime_set) == prime_fact


def have_distinct(index, consecutive_no, prime_fact):
    for i in range(0, consecutive_no):
        if not have_distinct_primes(index + i, prime_fact):
            return False

    return True


def distinct_prime_factors(consecutive_no, prime_fact):
    found = False
    i = 2
    while not found:
        if have_distinct(i, consecutive_no, prime_fact):
            return i

        i += 1


print(distinct_prime_factors(4, 4))  # 134043
