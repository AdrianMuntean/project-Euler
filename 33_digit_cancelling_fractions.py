import math


def simplify(num, den):
    for x in range(2, math.floor(math.sqrt(num))):
        while num % x == 0 and den % x == 0:
            num /= x
            den /= x

    return int(num), int(den)


def digit_cancelling_fractions():
    """
    Looking for numbers of form
     ax/xb = a/b
    """
    numerators = 1
    denominators = 1
    for num in range(10, 98):
        for den in range(num + 1, 99):
            div = num / den
            if den % 10 == 0:
                continue
            if div == (num // 10) / (den % 10) and (num % 10) == (den // 10):
                # print(f"{num}/{den}")
                numerators *= num
                denominators *= den

    return simplify(numerators, denominators)[1]


print(digit_cancelling_fractions())
