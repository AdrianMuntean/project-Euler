def self_powers(power, last_digits_count):
    """
    I'm just being lazy and let python do the job
    """

    sum = 0
    for i in range(1, power + 1):
        sum += i**i

    return f'{sum}'[-last_digits_count:]


print(self_powers(1000, 10))  # 9110846700
