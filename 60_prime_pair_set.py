import itertools
import copy
from math import comb
import string
from itertools import *
import math

smallest_sum = 0


def is_prime(n, primes):
    prime = primes.get(n)
    if prime:
        return True

    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def sieve(n):
    primes = {i: True for i in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):
        if primes.get(i):
            for x in range(i * i, n, i):
                primes.pop(x, None)

    return primes


def all_primes(pair, primes):
    for p in permutations(pair, 2):
        combined_number = int(str(f'{p[0]}{p[1]}'))
        if not is_prime(combined_number, primes):
            return False

    return True


def get_other_part(number, part_of_number):
    if len(str(number)) == len(str(part_of_number)):
        return 0
    index = str(number).find(str(part_of_number))
    return int(str(number)[index + len(str(part_of_number)):])


def could_be_split(part_1, part_2, number, primes):
    if len(str(part_1)) + len(str(part_2)) != len(str(number)):
        return False

    return primes.get(part_1) and primes.get(part_2)

def decompose(primes):
    pairs = {}
    for prime in primes.keys():
        factors = set()
        prime_part = 0
        for digit in map(int, str(prime)):
            prime_part = prime_part * 10 + digit
            other_part = get_other_part(prime, prime_part)
            if could_be_split(prime_part, other_part, prime, primes):
                factors.add(prime_part)
                factors.add(other_part)
                break

        if len(factors) > 0:
            pairs[prime] = factors

    return pairs


def re_compose(prime_pairs, no_pairs):
    min_required_appearances = (no_pairs - 1) * 2
    primes_appearances = {}
    for p in prime_pairs.values():
        for i in p:
            appearance = primes_appearances.get(i)
            if appearance:
                appearance += 1
            else:
                appearance = 1
            primes_appearances[i] = appearance
    
    filtered_appearances = {key: value for key, value\
                  in primes_appearances.items()\
                  if value >= min_required_appearances and key % 2 != 0}
    return filtered_appearances.keys()


def all_combinations_prime(combination, primes):
    for a in itertools.permutations(combination, 2):
        if not primes.get(int(f'{a[0]}{a[1]}')):
            return False
        
    return True

def extract_combinations(prime_pairs, no_pairs):
    min_required_appearances = (no_pairs - 1) * 2
    combinations = {}
    for k, pairs in prime_pairs.items():
        for prime in pairs:
            combination = combinations.get(prime) or set([])
            combination.add(k)
            combinations[prime] = combination

    filtered_appearances = {key: value for key, value\
                  in combinations.items()\
                  if min_required_appearances <= len(value)}
    return filtered_appearances


def extract_possible_pairs(prime_pairs, no_pairs):
    combinations = {}
    for k, pairs in prime_pairs.items():

        for prime in pairs:
            if prime % 2 == 0:
                continue
            combination = combinations.get(prime) or set([])
            list_from_set = list(prime_pairs[k])
            to_add = list_from_set[0] if prime != list_from_set[0] else list_from_set[1]
            combination.add(to_add)
            combinations[prime] = combination

    filtered_appearances = {key: value for key, value\
                  in combinations.items()\
                  if no_pairs - 1 <= len(value)}
    return filtered_appearances


def list_appears(item, list_to_check, prime_possible_pairs):
    new_list = []
    for i in list_to_check:
        adj_list = prime_possible_pairs.get(i) or []
        if item in adj_list:
            new_list.append(i)
    
    return new_list
        

def deep_check(items, pair_no, prime_possible_pairs, primes):
    adjacent_list = prime_possible_pairs.get(items[-1])
    if not adjacent_list:
        return []
    
    for i in items:
        if i not in adjacent_list and i != items[-1]:
            return []

    if len(items) >= pair_no:
        if not all_combinations_prime(items, primes):
            return []
        print(f'{items} with sum = {sum(items)}')
        global smallest_sum
        if sum(items) < smallest_sum or smallest_sum == 0:
            smallest_sum = sum(items)
            print(f'    found a new small! {items}')
            return []

        return []

    for item in adjacent_list:
        if item in items:
            continue
        new_items = copy.deepcopy(items)
        new_items.append(item)
        new_list = deep_check(new_items, pair_no, prime_possible_pairs, primes)
        if new_list is None:
            print('this is weird')
        if len(new_list) >= pair_no:
            return new_list

    return []


def prime_pair_set():
    # Compute the primes up to 10^5
    primes = sieve(10**6)
    pair_no = 4
    prime_pairs = decompose(primes)
    # prime_combine_dict = extract_combinations(prime_pairs, pair_no)
    prime_possible_pairs = extract_possible_pairs(prime_pairs, pair_no)

    # combinable_primes = re_compose(prime_pairs, pair_no)
    # last_comb = 0

    for k, v in prime_possible_pairs.items():
        for item in v:
            list_of_combinable = deep_check([k, item], pair_no, prime_possible_pairs, primes)
            # if len(list_of_combinable) == pair_no:
            #     print(list_of_combinable)
            #     print(sum(list_of_combinable))
            #     return
            
    # for combination in itertools.combinations(combinable_primes, pair_no):
    #     # if combination[0] == 3 and combination[1] == 7 and combination[2] == 109 and combination[3] == 673:
    #     #     print(combination)
    #     #     print('here')
    #     # print(combination)
    #     if combination[0] != last_comb:
    #         print(combination)
    #         last_comb = combination[0]
    #     if all_combinations_prime(combination, primes):
    #         print(sum(combination))
    #         break
    # new_dict = {}
    # for k, v in prime_possible_pairs.items():
    #     new_list = list_appears(k, v, prime_possible_pairs)
    #     if len(new_list) > 0:
    #         new_dict[k] = new_list

    # print(new_dict)
    # # print(prime_pairs)


print(prime_pair_set())
# print(get_other_part(123555, 1))
