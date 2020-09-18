import math

sum = 0

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
    if pent_values.get(x):
        return True
    n_floor = math.floor((math.sqrt(3) * math.sqrt(x * 2 + 1 // 12) + 0.5) / 3)
    n_round = math.ceil((math.sqrt(3) * math.sqrt(x * 2 + 1 // 12) + 0.5) / 3)
    
    return (n_floor * (3 * n_floor - 1) / 2 == x) or (n_round * (3 * n_round - 1) / 2 == x)


def try_find_petagonal_indexes(x):
    for i in pent.keys():
        value = pent_values.get(x - pent[i])
        if value and value != i:
            return (pent[i], pent[value])

    return (None, None)

def pentagon_numbers():
    d = 10**6
    for i in range(1, 10**7):
        pent_number_sum = pentagonal(i)
        (a, b) = try_find_petagonal_indexes(pent_number_sum)
        if a and b:
            # print(f'{a} and {b} have the sum penta')
            diff = abs(a - b)
            if is_pentagonal(diff):
                print(a, b)
        
    return d

print(pentagon_numbers())
