coins = [1, 2, 5, 10, 20, 50, 100, 200]
count = 0


def recur(n, out, i=0, index=0):
    if n == 0:
        # print(out[:index])
        global count
        count += 1

    for j in range(i, n):

        if j >= len(coins) or j >= len(out):
            break

        out[index] = coins[j]

        recur(n - coins[j], out, j, index + 1)


n = 200
out = [None] * n
recur(n, out)
print(count)  # 73682
