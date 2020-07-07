cache = {}


def collatz_sequence(n):
    len = 0
    index = n
    while index != 1:
        index = index / 2 if index % 2 == 0 else 3 * index + 1
        len = len + 1
        if index in cache:
            cache[n] = cache[index] + len
            return cache[n]

    return len


def largest_collatz_sequence(n):
    largest_chain = 0
    largest_chain_index = 0
    index = n
    while index > 1:
        chain_len = collatz_sequence(index)
        if largest_chain < chain_len:
            largest_chain = chain_len
            largest_chain_index = index
        index = index - 1

    return largest_chain_index


print(largest_collatz_sequence(1000000))
