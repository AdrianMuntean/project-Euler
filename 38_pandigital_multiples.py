def is_pandigital(n):
    digits = {}
    for digit in n:
        if digits.get(digit) or digit == "0":
            return False
        else:
            digits[digit] = True

    return len(digits) == 9


def biggest_possible(i):
    concatenated = ""
    for n in range(1, 10):
        prod = n * i
        if prod % 11 == 0 or len(concatenated) >= 9:
            break

        concatenated += str(i * n)
    return int(concatenated) if is_pandigital(concatenated) else 0


def pandigital_multiples():
    largest_number = 0
    for i in range(2, 10 ** 4):
        pandigital = biggest_possible(i)
        if pandigital > largest_number:
            largest_number = pandigital
    return largest_number


print(pandigital_multiples())  # 932718654
