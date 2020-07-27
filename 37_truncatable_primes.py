import math
import itertools


primes = {2: True, 3: True, 5: True, 7: True}
largest_value_checked = 2


def test_prime(n):
    last_digit = n % 10
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    global largest_value_checked
    if n > largest_value_checked:
        largest_value_checked = n
    primes[n] = True
    return True


def is_prime(n):
    cached_prime = primes.get(n, False)

    if largest_value_checked > n:
        return cached_prime

    return True if cached_prime else test_prime(n)


def primes_remove_left(n):
    for i in range(len(str(n)) - 1, 0, -1):
        number = n % 10 ** i
        if not is_prime(number):
            return False

    return True


def primes_remove_right(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10

    return True


def is_truncatable_prime(n):
    return primes_remove_right(n) and primes_remove_left(n)


def truncatable_primes(n):
    sum = 0
    count = 0
    for i in itertools.count(start=13):
        if is_truncatable_prime(i):
            sum += i
            count += 1
        if count >= n:
            break

    return sum


print(truncatable_primes(11))  # 748317
