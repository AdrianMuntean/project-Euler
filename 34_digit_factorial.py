factorials = {0: 1, 1: 1, 2: 2}


def fact(number):
    if number == 1 or number == 0:
        return 1
    return number * fact(number - 1)


def digit_factorial():
    sum = 0
    for number in range(10, 10**6):
        digit_sum = 0
        for x in map(int, str(number)):
            fac = factorials.get(x)
            if not fac:
                factorials[x] = fact(x)
                fac = factorials.get(x)
            digit_sum += fac

        if digit_sum == number:
            sum += number

    return sum


print(digit_factorial()) # 40730
