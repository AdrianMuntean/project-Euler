def powerful_digits_counts():
    count = 0
    for n in range(1, 10):  # x must be < 10 for this to happen, no need to search in for the big numbers
        for p in range(1, 100):
            power = n**p
            if len(str(power)) == p:
                count += 1

    return count


print(powerful_digits_counts())  # 49
