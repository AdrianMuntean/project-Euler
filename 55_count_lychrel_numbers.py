number_reverse1 = {}
number_reverse2 = {}


def is_palindrome(number):
    number_str = str(number)
    length = len(number_str)
    for i in range(0, len(number_str) // 2):
        if number_str[i] != number_str[length - 1 - i]:
            return False

    return True


def reverse(number):
    if number_reverse1.get(number):
        return number_reverse1.get(number)

    if number_reverse2.get(number):
        return number_reverse2.get(number)

    reverse = 0
    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        reverse = reverse * 10 + digit
        number_copy = number_copy // 10

    number_reverse1[number] = reverse
    number_reverse2[reverse] = number
    return reverse


def is_lychrel(number):
    for i in range(50):
        number += reverse(number)
        if is_palindrome(number):
            return False

    return True


def count_lychrel_numbers():
    count = 0
    for i in range(1, 10**4):
        if is_lychrel(i):
            count += 1

    return count


print(count_lychrel_numbers())  # 249

## better and improved versiondef reverse(number):

def reverse(number): return int( str(number)[::-1] )

def is_lychrel(number):
    for i in range(50):
        number += reverse(number)
        if number==reverse(number): 
            return 0
    return 1

print(sum(is_lychrel(number) for number in range(10**4)))
