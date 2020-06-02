import math

abunant_numbers = []


def can_be_expressed(number):
    for i in abunant_numbers:
        diff = number - i
        if diff in abunant_numbers:
            return True
    return False


def is_abundant(n):
    if n in abunant_numbers:
        return True
    if n == 1:
        return 1
    divs_sum = 1
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if n % i == 0:
            divs_sum += i + (n // i)
    if sqrt_n ** 2 == n:
        divs_sum += sqrt_n
    return divs_sum > n


def sum_of_non_abunant_number(n):
    sum = 1
    for number in range(2, n + 1):
        if is_abundant(number):
            abunant_numbers.append(number)
        if not can_be_expressed(number):
            sum += number
    return sum


print(sum_of_non_abunant_number(28123)) # 4179871
