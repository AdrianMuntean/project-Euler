import math

primes = {2: True, 3: True, 5: True, 7: True}


def is_prime(number):
    if primes.get(number):
        return True

    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    primes[number] = True
    return True


def spiral_primes():
    # just take an arbitrary upper limit
    diag_prime_count = 0
    for i in range(3, 10**5, 2):
        # lower right diag is never prime
        lower_right = i**2
        # we can start from this corner and work the others
        # since we can just traverse backwards
        if (is_prime(lower_right - 3 * (i - 1))):
            diag_prime_count += 1
        if (is_prime(lower_right - 2 * (i - 1))):
            diag_prime_count += 1
        if (is_prime(lower_right - (i - 1))):
            diag_prime_count += 1

        percent_primes = diag_prime_count / (2 * i - 1) * 100

        if percent_primes < 10:
            return i


print(spiral_primes())  # 26241
