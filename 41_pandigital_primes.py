import math


def is_consecutive_to(digits: {}, to, index=1):
    if index > to:
        return True

    if not digits.get(str(index)):
        return False

    return True and is_consecutive_to(digits, to, index + 1)


def is_pandigital(n):

    digits = {}
    largest_digit = 0
    for digit in n:
        if digits.get(digit) or digit == "0":
            return False
        else:
            digits[digit] = True
            int_digit = int(digit)
            if int_digit > largest_digit:
                largest_digit = int_digit

    return len(digits) == largest_digit and is_consecutive_to(digits, largest_digit)


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def prerequisites(n):
    if n % 10 == 9:
        return len(str(n)) == 9

    return True


def pandigital_primes():
    largest_number = 0
    for i in range(12, 10 ** 7):
        if prerequisites(i) and is_pandigital(str(i)) and is_prime(i):
            largest_number = i

    return largest_number


print(pandigital_primes())  # 7652413

