import math

sqrt_2 = math.sqrt(2)


def is_pentagonal(x):
    n_floor = math.floor((math.sqrt(3) * math.sqrt(x * 2 + 1 // 12) + 0.5) / 3)
    n_round = math.ceil((math.sqrt(3) * math.sqrt(x * 2 + 1 // 12) + 0.5) / 3)

    return (n_floor * (3 * n_floor - 1) / 2 == x) or (n_round * (3 * n_round - 1) / 2 == x)


def is_hexagonal(x):
    n_floor = math.floor(
        (math.sqrt(x + 1/8) + 1 / (2 * sqrt_2)) / sqrt_2)
    n_round = math.ceil((math.sqrt(x + 1/8) + 1 / (2 * sqrt_2)) / sqrt_2)

    return (n_floor * (2 * n_floor - 1) == x) or (n_round * (2 * n_round - 1) == x)


def triangle(x):
    return int(x * (x + 1) / 2)


def next_tri_penta_hexa():
    index = 285
    while True:
        index += 1
        number = triangle(index)
        if is_pentagonal(number) and is_hexagonal(number):
            return number


print(next_tri_penta_hexa())  # 1533776805
