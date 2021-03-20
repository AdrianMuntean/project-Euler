def read_from_file(file_name):
    numbers = []
    f = open(file_name, "r")
    for line in f:
        string_numbers = line.split(" ")
        numbers.append([int(n) for n in string_numbers])
    return numbers


def add_padding(numbers):
    padded_numbers = []
    length = len(numbers[-1])
    for i in numbers:
        padded_numbers.append([*i, *[0 for _ in range(len(i), length)]])

    return padded_numbers


def max_path(numbers):
    length = len(numbers[0]) - 1
    # start from bottom up
    for i in range(length - 1, -1, -1):
        for j in range(i + 1):
            # for each element, check the element right below the number
            # and right to the below number and sum them sum
            # e.g.
            # 1 0
            # 4 6 => for element 1 check which of his direct children
            # are bigger: 6 > 4 => the matrix becomes
            # 7 0
            # 4 6
            if numbers[i + 1][j] > numbers[i + 1][j + 1]:
                numbers[i][j] += numbers[i + 1][j]
            else:
                numbers[i][j] += numbers[i + 1][j + 1]

    # in the end the top element stores the max sum
    return numbers[0][0]


def max_path_from_file(file_name):
    numbers = read_from_file(file_name)
    # First, make this a square matrix by adding 0 padding
    numbers = add_padding(numbers)
    # Then find the max path sum using dynamic programming
    return max_path(numbers)


print(max_path_from_file("p067_triangle.txt"))  # 7273