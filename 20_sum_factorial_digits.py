def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def count_digits(n):
    sum = 0
    for digit in map(int, str(n)):
        sum += digit
    return sum
    
print(count_digits(fact(100))) # 648
