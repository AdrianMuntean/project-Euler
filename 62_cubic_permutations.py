def compute_cubes(upper_limit):
    digits_to_cube = {}
    for i in range(100, upper_limit):
        cube = i**3
        # the key of the dict is the sorted string made of the digits
        digits = [i for i in str(cube)]
        digits = ''.join(sorted(digits))

        value = digits_to_cube.get(digits) or []
        value.append(cube)
        digits_to_cube[digits] = value

    return digits_to_cube


def cubic_permutations():
    digits_to_cube = compute_cubes(9000)
    for k, v in digits_to_cube.items():
        if len(v) == 5:
            return v[0]


# solution generated in 200 millis
print(cubic_permutations())  # 127035954683
