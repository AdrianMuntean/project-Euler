import copy


def compute_digits(number):
    digits = {}
    for i in map(int, str(number)):
        digits[i] = True

    return digits


def same_digits_multiple(number, digits):
    digits_copy = copy.deepcopy(digits)
    for i in map(int, str(number)):
        if digits_copy.get(i):
            digits_copy[i] = False
        else:
            return False

    return True


def multiple_has_same_digits(number):
    digits = compute_digits(number)
    for i in range(2, 6):
        if not same_digits_multiple(i * number, digits):
            return False

    return True


def permuted_multiples():
    i = 100
    deg = 2
    while True:
        # just check number which multiplied with 6 have the same length
        if len(str(6 * i)) > len(str(i)):
            deg += 1
            i = 10**deg
            continue
        if multiple_has_same_digits(i):
            return i
        else:
            i += 1


print(permuted_multiples())  # 142857
