# () => () => ()
#       I  /  |
#       ()    ()
#       I
#       ()

pos_gen = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1)]
pos = [(0, 0), (0, 1), (0, 2), (1, 2), (0, 2), (1, 1), (2, 1), (1, 1), (0, 1)]
sols = set()


def is_valid(arr):
    flat_list = [item for sublist in arr for item in sublist]
    for j in range(1, 7):
        if flat_list.count(j) > 1:
            return False
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
    a = array[0][0]
    b = array[1][2]
    c = array[2][1]
    s = 0
    m = min([a, b, c])
    if m == a:
        s = 0
    if m == b:
        s = 3
    if m == c:
        s = 6

    for i in range(s, s + len(pos)):
        p = pos[i % len(pos)]
        if i > 0 and i % 3 == 0:
            store.append(sv)
            sv = ""
        sv = f"{sv}{array[p[0]][p[1]]}"

    store.append(sv)
    string_sol = "".join(store)
    sols.add(string_sol)


def gen_ring(j, array=[[], [], []]):
    if j >= len(pos_gen):
        if is_valid(array):
            store_solution(array)
            # pretty_print(array)
        else:
            # print("not valid")
            # print(array)
            pass
        return
    c_pos = pos_gen[j]
    for i in range(1, 7):
        # if i in array[0] or i in array[1] or i in array[2]:
        #     continue
        array[c_pos[0]][c_pos[1]] = i
        gen_ring(
            j + 1,
            array=array,
        )


def compute_ring():
    arr = [[None] * 3 for i in range(3)]
    for i, p in enumerate(pos_gen):
        gen_ring(i, arr)
        # if is_valid(arr):
        #     print(arr)
        #     print("is valid")
        # else:
        #     print("not valid")


def biggest_solution():
    largest = 0
    for i in sols:
        if int(i) > largest:
            largest = int(i)

    print(largest)


compute_ring()
print(biggest_solution())
# print(is_valid([[4, 6, 8], [None, 7, 3], [None, 5, None]]))
