def distinct_powers(n):
    powers = {}
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            elem = a**b
            powers[elem] = 1

    return len(powers)


print(distinct_powers(100)) # 9183
