import math


def int_right_triangles(n):
    max_triangles = 0
    saved_p = 0
    for p in range(100, n):
        triangles = 0

        for a in range(20, p // 3):
            for b in range(a, p // 2):
                c = math.sqrt(a ** 2 + b ** 2)
                if a + b + c == p:
                    triangles += 1

        if triangles > max_triangles:
            max_triangles = triangles
            saved_p = p

    return saved_p


print(int_right_triangles(1000))
