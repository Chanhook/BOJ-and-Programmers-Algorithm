import sys

input = sys.stdin.readline
t = int(input().strip())


def find_k(m, n, x, y):
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k

        k += m

    return -1


for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(find_k(m, n, x, y))