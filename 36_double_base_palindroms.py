import math


def binary(number):
    num_bits = int(math.log(number, 2) + 1)
    return [(number >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]


def is_palindrome(number_arr):
    length = len(number_arr)
    for i in range(0, length):
        if number_arr[i] != number_arr[length - 1 - i]:
            return False

    return True


def double_base_palindroms():
    sum = 0
    for number in range(1, 10 ** 6, 2):
        if is_palindrome([int(x) for x in str(number)]) and is_palindrome(binary(number)):
            sum += number

    return sum


print(double_base_palindroms())  # 872187
