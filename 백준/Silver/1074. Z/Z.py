n, r, c = map(int, input().split())


def recursiveSearch(n, r, c):
    if n == 0:
        return 0

    half_size = 2**(n-1)
    if r < half_size and c < half_size:
        return recursiveSearch(n-1, r, c)
    elif r < half_size and c >= half_size:
        return 1*half_size*half_size+recursiveSearch(n-1, r, c-half_size)
    elif r >= half_size and c < half_size:
        return 2*half_size*half_size+recursiveSearch(n-1, r-half_size, c)
    elif r >= half_size and c >= half_size:
        return 3*half_size*half_size+recursiveSearch(n-1, r-half_size, c-half_size)


print(recursiveSearch(n, r, c))
