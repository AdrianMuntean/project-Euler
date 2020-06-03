import math
import time

start_time = time.time()

values = [x for x in range(10)]
permutations = []


def swap(array, i, j):
    t = array[i]
    array[i] = array[j]
    array[j] = t


def perm(array, n, i):
    if i == n:
        permutations.append("".join(map(str, array)))
        return

    for index in range(i, n):
        swap(array, i, index)
        perm(array, n, i + 1)
        swap(array, i, index)


perm(values, len(values), 0)
permutations.sort()
print(permutations[999999])  # 2783915460
print("--- %s seconds ---" % (time.time() - start_time))
