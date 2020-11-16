import copy

t = {}
s = {}
p = {}
h = {}
hep = {}
o = {}

dicts = {1: t, 2: s, 3: p, 4: h, 5: hep, 6: o}

formulas = [
    (lambda i: i * (i + 1) / 2, 1),
    (lambda i: i * i, 2),
    (lambda i: i * (3 * i - 1) / 2, 3),
    (lambda i: i * (2 * i - 1), 4),
    (lambda i: i * (5 * i - 3) / 2, 5),
    (lambda i: i * (3 * i - 2), 6),
]


def pre_compute_numbers():
    for i in range(15, 200):
        for f, name in formulas:
            p = int(f(i))
            if 999 < p < 10000:
                dicts[name][p] = True


def get_next_starts_with(digits, items_selected):
    nexts = []
    if len(items_selected) == 6:
        next_i = items_selected[0]
        numbers = dicts[next_i]
        for i in range(10, 100):
            composed_number = int(f'{digits}{i}')
            if numbers.get(composed_number):
                nexts.append((composed_number, next_i))

    next_index = next(filter(lambda x: x not in items_selected, (n for n in range(1, 7))), None)

    new_items = copy.deepcopy(items_selected)
    while next_index:
        numbers = dicts[next_index]
        for i in range(10, 100):
            composed_number = int(f'{digits}{i}')
            if numbers.get(composed_number):
                nexts.append((composed_number, next_index))

        new_items.append(next_index)
        next_index = next(filter(lambda x: x not in new_items, (n for n in range(1, 7))), None)
    return nexts


def generate_cycle(current_items=[], items_selected=[]):
    if len(items_selected) > 6:
        return current_items

    if len(current_items) > 0:
        last_digits = current_items[-1] % 100
        possible_next_values = get_next_starts_with(last_digits, items_selected)

        if len(items_selected) == 6:
            if current_items[0] in map(lambda x: x[0], possible_next_values):
                return current_items
            else:
                return []

        for p, index in possible_next_values:
            new_items = copy.deepcopy(current_items)
            new_items.append(p)
            new_index = copy.deepcopy(items_selected)
            new_index.append(index)
            cycle = generate_cycle(new_items, new_index)
            if len(cycle) == 6:
                return cycle

        return []
    else:
        for i in range(1, 7):
            for key in dicts[i].keys():
                new_items = copy.deepcopy(current_items)
                new_items.append(key)
                new_index = copy.deepcopy(items_selected)
                new_index.append(i)
                cycle = generate_cycle(new_items, new_index)
                if len(cycle) == 6:
                    return cycle

        return []


def cyclical_figurate_numbers():
    pre_compute_numbers()
    cycle = generate_cycle()
    print(f'cycle = {cycle}')  # [8256, 5625, 2512, 1281, 8128, 2882]
    return sum(cycle)


print(cyclical_figurate_numbers())  # 28684
