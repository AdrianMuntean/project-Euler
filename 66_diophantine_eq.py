import itertools
import math


def find_coef_brute_force(d):
    """
    Really dummy frute force method. 
    Takes forever to compute
    """
    for x in itertools.count(int(math.sqrt(d + 1))):
        a = x ** 2 - 1
        if a % d != 0:
            continue
        y_squared = (x ** 2 - 1) / d
        y = math.sqrt(y_squared)
        if y.is_integer():
            return x


def find_coef(d):
    """
    Bhaskara II (1114−1185) developed a cyclic algorithm (called chakravala method)
    Using this algo takes about 40-50ms to compute the answer 
    http://www.kurims.kyoto-u.ac.jp/EMIS/journals/GMN/yahoo_site_admin/assets/docs/1_GMN-8492-V28N2.190180001.pdf in this paper the method is described 
    """
    ai_1 = 0
    bi_1 = 1
    ci_1 = d
    ai = 1
    bi = 0
    ci = 1
    while(True):
        qi = int((math.sqrt(d - ci_1 * ci) + math.sqrt(d)) / ci)
        ci1 = 2 * qi * math.sqrt(d - ci_1 * ci) + ci_1 - qi**2 * ci
        aux_a = ai
        aux_b = bi
        aux_c = ci
        ai = qi * ai + ai_1
        bi = qi * bi + bi_1
        ci = ci1
        ai_1 = aux_a
        bi_1 = aux_b
        ci_1 = aux_c

        if ai**2 - d * bi**2 == 1:
            return ai


def diophantine_eq():
    largest_x = 0
    saved_d = 0
    for d in range(2, 1000):
        if math.sqrt(d).is_integer():
            continue
        x = find_coef(d)
        if x > largest_x:
            largest_x = x
            saved_d = d

    return saved_d


print(diophantine_eq())  # 661
