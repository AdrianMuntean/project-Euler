import math
import copy


def sieve(n):
    primes = {i: True for i in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):
        if primes.get(i):
            for x in range(i * i, n, i):
                primes.pop(x, None)

    return primes


def count_primes(number, primes):
    count = 0
    for i in range(0, 10):
        number_string = ''.join(number).replace('*', f'{i}')
        number_int = int(number_string)
        if len(str(number_int)) != len(number):
            continue
        if primes.get(number_int):
            count += 1

    return (count, number)


def find_max(number, digits, index, max, primes):
    if digits == 0:  # time to count the primes for the vatiation
        primes_count = count_primes(number, primes)
        if primes_count[0] > max[0]:
            max[0] = primes_count[0]
            max[1] = primes_count[1]

        return

    for i in range(index, len(number) - digits):
        number_copy = copy.deepcopy(number)
        number_copy[i] = '*'
        find_max(number_copy, digits - 1, i + 1, max, primes)


def matches_pattern(prime_number, pattern):
    # we need this function so that examples like 
    # *2*3*3 and number 120383 should not match
    for i in range(0, 10):
        number_string = ''.join(pattern).replace('*', f'{i}')
        if int(number_string) == prime_number:
            return True

    return False


def consecutive_prime_sum(family_numbers):
    # Compute the primes up to 10^6
    primes = sieve(10**6)
    # iterate over the primes and check
    for k in primes.keys():
        for i in range(1, len(str(k))):
            # we can variate any number of digits,
            # but not the last
            max = [0, 0]  # 0 is the count and 1 is the pattern
            find_max(list(str(k)), i, 0, max, primes)
            if max[0] == family_numbers and matches_pattern(k, max[1]):
                return k


print(consecutive_prime_sum(8))  # 121313
