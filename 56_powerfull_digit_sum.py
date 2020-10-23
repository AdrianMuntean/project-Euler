def variations():
    for a in range(100):
        for b in range(100):
            yield sum([int(x) for x in str(a**b)])


print(max([digit_sum for digit_sum in variations()])) # 972
