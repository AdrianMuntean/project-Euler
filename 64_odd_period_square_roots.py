# Need to revisit this problem, not really original code :|
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
import math
import itertools


def is_square_root(r):
    p = int(math.sqrt(r))
    if p * p == r:
        return True, None
    return False, p


def cf_period(r):
    is_square, p = is_square_root(r)
    if is_square:
        return 0
    q = 1
    remainders = dict()

    for pos in itertools.count(1):
        q = (r-(p*p))/q
        floor = int((math.sqrt(r)+p) / float(q))
        p = -1 * (p - (floor*q))
        if (p, q) in remainders:
            return pos-remainders[p, q]
        remainders[p, q] = pos


print(len([x for x in range(2, 10001) if cf_period(x) % 2 == 1]))  # 1322
