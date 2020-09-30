import math

already_found_number = 1487


def is_prime(n):
    d = 3
    while n // d > math.sqrt(n):
        if n % d == 0:
            return False
        d += 2

    return True


def compute_perm_dict(number):
    digits = {}
    for i in str(number):
        if digits.get(i):
            digits[i] += 1
        else:
            digits[i] = 1

    return digits


def is_perm(base, number):
    digits = compute_perm_dict(number)

    return digits == base


def unusual_sequence(starting_value):
    perm_base = compute_perm_dict(starting_value)
    for i in range(1, 3):
        number = starting_value + i * 3330
        if not is_prime(number) or not is_perm(perm_base, number):
            return False

    return True


def prime_permutations():
    for i in range(1001, 3339, 2):  # only take the odd numbers
        if not is_prime(i) or i == already_found_number:
            continue

        if unusual_sequence(i):
            return f'{i}{i + 3330}{i + 6660}'


print(prime_permutations())  # 296962999629
