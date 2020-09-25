import math

prime = {
    1: True,
    2: True,
    3: True,
    5: True,
    7: True,
}


def is_prime(n):
    if prime.get(n):
        return True

    d = 3
    while n // d > math.sqrt(n):
        if n % d == 0:
            return False
        d += 2

    prime[n] = True
    return True


def check_conjecture(n):
    for a in range(1, 10**3):
        diff = n - 2 * a**2
        if diff < 0:
            return False
        if is_prime(diff):
            return True

    return False


def smallest_odd_composite():
    """
    Any number that is not prime is composite
    """
    index = 9
    while True:
        index += 2
        if not is_prime(index):
            if not check_conjecture(index):
                print(index)
                return


print(smallest_odd_composite())  # 1533776805
