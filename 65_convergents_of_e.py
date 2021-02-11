def get_continued_fraction_constant(index):
    """
    e = [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...], therefore we can find out 
    the constant pretty easy
    """
    return (index // 3 + 1) * 2 if index % 3 == 1 else 1


def compute_ith_convergent(n):
    a = [0, 0]
    for i in range(n - 2, -1, -1):
        constant = get_continued_fraction_constant(i)

        if a[0] == 0:
            a[0] += 1
            a[1] += constant
        elif n - 2 - i < 2:  # after the first 2 computations, flip after every computation
            a[0] = constant * a[1] + a[0]
        else:
            a[0], a[1] = a[1], a[0]
            a[0] = constant * a[1] + a[0]

    a[0], a[1] = a[1], a[0]
    a[0] = 2 * a[1] + a[0]
    return a


print(sum([i for i in map(int, str(compute_ith_convergent(100)[0]))]))  # 272
