def spiral_diag(n):
    sum = 1
    for i in range(1, (n + 1) // 2):
        sum += (2 * i + 1)**2 + (2 * i + 1)**2 - 2 * i + \
            (2 * i)**2 + 1 + (2 * i)**2 + 1 - 2 * i

    return sum


print(spiral_diag(1001)) # 669171001
