import itertools
import math


def find_coef(d):
    for x in itertools.count(int(math.sqrt(d + 1))):
        a = x ** 2 - 1
        if a % d != 0:
            continue
        y_squared = (x ** 2 - 1) / d
        y = math.sqrt(y_squared)
        if y.is_integer():
            return x


def diophantine_eq():
    """
    Really dummy frute force method. 
    Takes forever to compute
    """
    largest_x = 0
    saved_d = 0
    for d in range(2, 100):
        if math.sqrt(d).is_integer():
            continue
        x = find_coef(d)
        if x > largest_x:
            largest_x = x
            saved_d = d
        print(d)

    return saved_d


print(diophantine_eq())  # 661
