last_iteration = (1, 1)


def iterations(no_iterations):
    """
    We can find each number by adding 1 + 1/(1 + last)
    This can be further simplified to 
    (2 * numerator + denominator) / (numerator + denominator), where 
    numerator and denominator are of the last one, starting with 1
    """
    for a in range(no_iterations):
        global last_iteration
        result = (last_iteration[0] + 2 * last_iteration[1],
                  last_iteration[0] + last_iteration[1])
        last_iteration = result
        yield result


print(sum(list((map(lambda x: len(str(x[0])) > len(str(x[1])), [
      digit_sum for digit_sum in iterations(1000)])))))  # 153
