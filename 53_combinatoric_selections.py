fact_cache = [1, 1, 2, 6]


def _compute_factorial(number):
    for i in range(number - 1, -1, -1):
        if len(fact_cache) <= i:
            continue

        return number * fact_cache[i]


def compute_fact(number):
    if len(fact_cache) > number:
        return fact_cache[number]

    fact = _compute_factorial(number)

    fact_cache.append(fact)
    return fact


def combination(n, k):
    n_fact = compute_fact(n)
    k_fact = compute_fact(k)
    n_k_diff = compute_fact(n-k)
    return n_fact / (k_fact * n_k_diff)


def combinatoric_selections():
    count = 0
    for n in range(1, 101):
        for k in range(1, n):
            if combination(n, k) >= 10**6:
                count += 1
    return count


print(combinatoric_selections())  # 4075
