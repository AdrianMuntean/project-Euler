import math

sum = 0

pent = {}
pent_values = {}

def pentagonal(x):
    if pent.get(x):
        return pent[x]
    
    p = int(x * (3 * x - 1) / 2)
    pent[x] = p
    pent_values[p] = True
    return p

def is_pentagonal(x):
    if pent_values.get(x):
        return True
    n_floor = math.floor((math.sqrt(3) * math.sqrt(x * 2 + 1 // 12) + 0.5) / 3)
    n_round = math.ceil((math.sqrt(3) * math.sqrt(x * 2 + 1 // 12) + 0.5) / 3)
    
    return (n_floor * (3 * n_floor - 1) / 2 == x) or (n_round * (3 * n_round - 1) / 2 == x)


def pentagon_numbers():
    d = 10**6
    for i in range(1, 10**7):
        for j in range(i + 1, 10**7):
            p1 = pentagonal(i)
            p2 = pentagonal(j)

            if is_pentagonal(p1 + p2) and is_pentagonal(abs(p1 - p2)):
                diff = abs(p1 - p2)
                if diff < d:
                    d = diff
                    print(f'found one : {d}')
        
    return d

print(pentagon_numbers())
