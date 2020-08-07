# just use Python's power for this
def champernownes_constant():
    s = " "
    for i in range(1, 10 ** 6 + 1):
        s += str(i)

    prod = 1
    p = 1
    while p <= 10 ** 6:
        prod *= int(s[p])
        p *= 10

    return prod


print(champernownes_constant())  # 210

