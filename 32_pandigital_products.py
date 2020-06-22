def is_pandigital(n, m='', p='', complete=False):
    a = [False] * 9
    for c in map(int, str(n) + str(m) + str(p)):
        if a[c - 1] or c == 0:
            return False
        a[c - 1] = True

    if complete:
        return not False in a

    return True


def pandigital_products():
    sum = 0
    pandigital_operators = []
    for s in range(1, 987):
        if not is_pandigital(s):
            continue

        for t in range(1, 9876):
            if not is_pandigital(s, t):
                continue

            prod = s * t
            if is_pandigital(s, t, prod, complete=True):

                if prod not in pandigital_operators:
                    print(f'{s} * {t} = {prod}')
                    sum += prod
                    pandigital_operators.append(prod)

    return sum


print(pandigital_products()) # 45228
