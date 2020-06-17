def digit_n_powers(n):
    number = 10
    sum = 0
    for number in range(10, 10**6):
        copy = number
        digit_sum = 0
        while copy > 0:
            digit = copy % 10
            copy = copy // 10
            digit_sum += digit**n
        if digit_sum == number:
            sum += number

    return sum


print(digit_n_powers(5))  # 443839
