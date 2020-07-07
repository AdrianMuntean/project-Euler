import math


def factorize(number):
    prime_factors = {}
    for factor in range(number, 1, -1):
        number_copy = factor
        prime_factor = 2
        while (number_copy > 1 and prime_factor <= number_copy):
            if number_copy % prime_factor == 0:
                number_copy = number_copy / prime_factor
                if factor not in prime_factors.keys():
                    prime_factors[factor] = {
                        prime_factor: prime_factors.get(factor, {}).get(prime_factor, 0) + 1}
                else:
                    prime_factors[factor].update({
                        prime_factor: prime_factors.get(
                            factor, {}).get(prime_factor, 0) + 1
                    })
            else:
                prime_factor = prime_factor + 1
    
    return prime_factors


def get_smallest_prime_factors(prime_factors):
    smallest_prime_factors = {}

    for key in prime_factors:
        factors = prime_factors[key]
        for prim_factor in factors:
            if prim_factor not in smallest_prime_factors:
                smallest_prime_factors[prim_factor] = factors[prim_factor]
            else:
                if smallest_prime_factors[prim_factor] < factors[prim_factor]:
                    smallest_prime_factors[prim_factor] = factors[prim_factor]

    return smallest_prime_factors


def smallest_mult(number):
    prime_factors = factorize(number)

    smallest_prime_factors = get_smallest_prime_factors(prime_factors)
    
    product = 1
    for prime_fact in smallest_prime_factors:
        product = product * math.pow(prime_fact, smallest_prime_factors[prime_fact])
    return int(product)
    

print(smallest_mult(20))
