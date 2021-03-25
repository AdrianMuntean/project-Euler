# () => () => ()
#       I  /  |
#       ()    ()
#       I
#       ()

pos_gen = [
    (1, 0),
    (1, 1),
    (1, 2),
    (0, 2),
    (2, 1),
    (2, 2),
    (3, 1),
    (3, 2),
    (3, 0),
    (2, 0),
]
pos = [
    (1, 0),
    (1, 1),
    (1, 2),
    (0, 2),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 1),
    (3, 1),
    (3, 2),
    (3, 1),
    (3, 0),
    (2, 0),
    (3, 0),
    (1, 1),
]
sols = set()


def is_valid(arr):
    p_sum = 0
    sum = 0
    for i, p in enumerate(pos):
        if i > 0 and i % 3 == 0:
            if p_sum != 0 and p_sum != sum:
                return False
            p_sum = sum
            sum = 0
        e = arr[p[0]][p[1]]
        sum += e

    if p_sum != sum:
        return False
    return True


def pretty_print(array):
    s = ""
    for p in pos:
        s = f"{s},{array[p[0]][p[1]]}"

    print(s)


def store_solution(array):
    store = []
    sv = ""
    a = array[1][0]
    b = array[0][2]
    c = array[2][2]
    d = array[3][2]
    e = array[2][0]
    s = 0
    m = min([a, b, c, d, e])
    if m == a:
        s = 0
    if m == b:
        s = 3
    if m == c:
        s = 6
    if m == d:
        s = 9
    if m == e:
        s = 12

    for i in range(s, s + len(pos)):
        p = pos[i % len(pos)]
        if i > 0 and i % 3 == 0:
            store.append(sv)
            sv = ""
        sv = f"{sv}{array[p[0]][p[1]]}"

    store.append(sv)
    string_sol = "".join(store)
    sols.add(string_sol)


def available_digits(array, c_pos):
    existing_digits = []
    for p in pos:
        if p == c_pos:
            break
        existing_digits.append(array[p[0]][p[1]])
    return [item for item in range(1, 11) if item not in existing_digits]


def gen_ring(j, array=[[], [], []]):
    if j >= len(pos_gen):
        if is_valid(array):
            store_solution(array)
            pretty_print(array)
        return
    c_pos = pos_gen[j]
    for i in available_digits(array, c_pos):
        array[c_pos[0]][c_pos[1]] = i
        gen_ring(
            j + 1,
            array=array,
        )


def compute_ring():
    arr = [[None] * 3 for _ in range(4)]
    for i, _ in enumerate(pos_gen):
        gen_ring(i, arr)


def biggest_solution():
    largest = 0
    for i in sols:
        if int(i) // 10 ** (len(i) - 5) > largest // 10 ** (len(str(largest)) - 5):
            largest = int(i)

    print(largest)


compute_ring()
print(biggest_solution())  # 6531031914842725
# print(is_valid([[None, None, 10], [6, 5, 3], [7, 1, 9], [2, 4, 8]]))
