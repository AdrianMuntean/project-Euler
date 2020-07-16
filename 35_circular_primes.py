import math

primes = {}
largest_value_checked = 2
non_primes_digits = [0, 2, 4, 5, 6, 8]


def test_prime(n, primary):
    last_digit = n % 10
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    global largest_value_checked
    if primary:
        largest_value_checked = n
    primes[n] = True
    return True


def is_prime(n, primary):
    cached_prime = primes.get(n, False)

    if largest_value_checked > n and primary:
        return cached_prime

    return True if cached_prime else test_prime(n, primary)


def get_rotations(n):
    """
        Return only set of rotation which have the chance of being prime
    """
    rotations = [n]
    for x in range(len(str(n)) - 1):
        last_digit = n % 10

        if last_digit in non_primes_digits:
            return None
        rotation = last_digit * 10 ** (len(str(n)) - 1) + n // 10
        if rotation not in rotations:
            rotations.append(rotation)
        n = rotation

    return rotations


def circular_prime():
    count = 4
    for n in range(10 ** 1, 10 ** 6):
        rotations = get_rotations(n)
        if not rotations:
            continue
        all_prime = True
        for rotation in rotations:
            if not is_prime(rotation, primary=rotation == n):
                all_prime = False
                break
        if all_prime:
            count += 1

    return count  # 55


print(circular_prime())
