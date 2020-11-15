import itertools
import copy
from itertools import *
import math

smallest_sum = 0
biggest_prime = 0
found_pairs = []
not_primes = {}


def is_prime(n, primes):
    """
    Use the primes dict computed using the Sieve. Only check for the numbers which are higher than the max
    """
    prime = primes.get(n)
    if prime:
        return True
    else:
        if n < biggest_prime:
            return False
        else:
            not_prime = not_primes.get(n)
            if not_prime:
                return False

    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            not_primes[n] = False
            return False

    return True


def sieve(n):
    primes = {i: True for i in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):
        if primes.get(i):
            for x in range(i * i, n, i):
                primes.pop(x, None)

    # remove 2 and 5 cause no number ending with either of these 2 is going to be prime
    del primes[2]
    del primes[5]
    return primes


def deep_check(items, pair_no, prime_possible_pairs, primes, end_at_first=True):
    """ Use backtracking to check for all the combinations. This could be replaced with itertools.permutations
    and some logic. 
    """
    adjacent_list = prime_possible_pairs.get(items[-1])
    if not adjacent_list:
        return []

    # If all the elements are in the list of the others, then it's fine, carry on
    for i in items:
        adj = prime_possible_pairs.get(i) or []
        for j in items:
            if i == j:
                continue
            if j not in adj:
                return []

    if len(items) >= pair_no:
        sum_ = sum(items)
        if sum_ in found_pairs:
            return []
        else:
            found_pairs.append(sum_)
        print(f'{items} with sum = {sum(items)}')
        global smallest_sum

        if sum(items) < smallest_sum or smallest_sum == 0:
            smallest_sum = sum(items)
            print(f'    found a new smaller combination! {items}')
            if end_at_first:
                return items
            return []

        return []

    # Core backtracking logic
    for item in adjacent_list:
        if item in items:
            continue
        new_items = copy.deepcopy(items)
        new_items.append(item)
        new_list = deep_check(new_items, pair_no, prime_possible_pairs, primes)
        if len(new_list) >= pair_no:
            return new_list

    return []


def make_pairs(primes):
    pairs = {}
    for i in itertools.combinations(primes.keys(), 2):
        first = i[0]
        second = i[1]
        if is_prime(int(f'{first}{second}'), primes):
            p = pairs.get(first) or []
            if second not in p:
                p.append(second)
            pairs[first] = p
        if is_prime(int(f'{second}{first}'), primes):
            p = pairs.get(second) or []
            if first not in p:
                p.append(first)
            pairs[second] = p

    return pairs


def prime_pair_set():
    # Compute the primes up to 10^4
    primes = sieve(10**4)
    global biggest_prime
    biggest_prime = list(primes.keys())[-1]
    pair_no = 5

    pairs = make_pairs(primes)
    for k, v in pairs.items():
        for item in v:
            list_of_combinable = deep_check([k, item], pair_no, pairs, primes)
            if len(list_of_combinable) == pair_no:
                return sum(list_of_combinable)


#  takes around 2 minutes, need to improve this
print(prime_pair_set())  # 26033 is the sum of [5197, 13, 5701, 6733, 8389]
