import math

sum = 0

ranges = {
    17: [1, 58],
    13: [1, 76],
    11: [1, 90],
    7: [2, 142],
    5: [2, 199],
    3: [4, 333],
    2: [5, 499],
}


def distinct_digits(n):
    digits = {}
    for digit in n:
        if digits.get(digit):
            return False
        else:
            digits[digit] = True

    return True


def add_missing_digit(number):
    for i in range(1, 10):
        if str(i) not in number:
            return f"{i}{number}"

    return number


def sub_string_div(index=0, number_str=""):
    n = list(ranges.keys())[index]
    for l in range(ranges[n][0], ranges[n][1]):
        prod = n * l
        str_prod = f"0{prod}" if prod < 100 else str(prod)
        new_number_str = f"{prod//100}{number_str}"
        if index != 0:
            if not str_prod[1:] == number_str[0:2]:
                continue
        else:
            new_number_str = str_prod

        if distinct_digits(str_prod) and distinct_digits(new_number_str):
            if index == len(ranges.keys()) - 1:
                global sum
                sum += int(add_missing_digit(new_number_str))
            else:
                sub_string_div(index + 1, new_number_str)


sub_string_div()
print(sum)  # 16695334890
