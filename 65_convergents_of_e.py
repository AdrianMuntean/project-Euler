def get_continued_fraction_constant(index):
    """
    e = [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...], therefore we can find out 
    the constant pretty easy
    """
    group = index // 3 + 1
    rest = index % 3
    return group * 2 if rest == 1 else 1


def swap_function_places(a):
    aux = a[0]
    a[0] = a[1]
    a[1] = aux

    return a


def compute_ith_convergent(n):
    a = [0, 0]
    for i in range(n - 2, -1, -1):
        constant = get_continued_fraction_constant(i)

        if a[0] == 0:
            a[0] += 1
            a[1] += constant
        elif n - 2 - i < 2:
            a[0] = constant * a[1] + a[0]
        else:
            a = swap_function_places(a)
            a[0] = constant * a[1] + a[0]

    a = swap_function_places(a)
    a[0] = 2 * a[1] + a[0]
    return a


def sum_digit(n):
    # we can safely assume that the num and den don't have common factors
    return sum([i for i in map(int, str(n))])


print(sum_digit(compute_ith_convergent(100)[0]))  # 272
