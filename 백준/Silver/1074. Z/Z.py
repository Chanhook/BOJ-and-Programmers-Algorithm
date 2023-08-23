def recursive(n, r, c):
    if n == 0:
        return 0

    square = 2 ** (n - 1)
    if r < square and c < square:
        return recursive(n - 1, r, c)
    elif r < square and c >= square:
        return square * square + recursive(n - 1, r, c - square)
    elif r >= square and c < square:
        return 2 * square * square + recursive(n - 1, r - square, c)
    else:
        return 3 * square * square + recursive(n - 1, r - square, c - square)


N, r, c = map(int, input().split())
print(recursive(N, r, c))
