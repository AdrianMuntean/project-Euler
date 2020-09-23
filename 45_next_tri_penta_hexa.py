import math

sqrt_2 = math.sqrt(2)


def pentagonal(x):
    return int(x * (3 * x - 1) / 2)


def is_hexagonal(x):
    n_floor = math.floor(
        (math.sqrt(x + 1/8) + 1 / (2 * sqrt_2)) / sqrt_2)
    n_round = math.ceil((math.sqrt(x + 1/8) + 1 / (2 * sqrt_2)) / sqrt_2)

    return (n_floor * (2 * n_floor - 1) == x) or (n_round * (2 * n_round - 1) == x)


def next_tri_penta_hexa():
    """
    We can safely ignore the triangle numbers cause all the pentagon numbers are also triangle numbers
    """
    index = 285
    while True:
        index += 1
        number = pentagonal(index)
        if is_hexagonal(number):
            return number


print(next_tri_penta_hexa())  # 1533776805
