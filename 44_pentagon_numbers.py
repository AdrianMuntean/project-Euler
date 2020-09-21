import math
from itertools import islice

pent = {}
pent_values = {}


def pentagonal(x):
    if pent.get(x):
        return pent[x]

    p = int(x * (3 * x - 1) / 2)
    pent[x] = p
    pent_values[p] = x
    return p


def is_pentagonal(x):
    return pent_values.get(x)


def find_all_petagonal_indexes(x):
    pairs = []
    for k, v in islice(pent.items(), len(pent) // 2):
        value = pent_values.get(x - v)
        if value and value != k:
            pairs.append((v, pent[value]))

    return pairs


def pentagon_numbers():
    d = 10**6
    for i in range(10**3, 10**5):
        pent_number_sum = pentagonal(i)
        pairs = find_all_petagonal_indexes(pent_number_sum)
        for (a, b) in pairs:
            diff = abs(a - b)
            if is_pentagonal(diff) and d < diff:
                d = diff
                print(diff)

    return d


print(pentagon_numbers())  # 5482660
