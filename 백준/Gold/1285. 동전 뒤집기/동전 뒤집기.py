import sys

input = sys.stdin.readline
n = int(input().strip())
arr = [list(input().strip()) for _ in range(n)]
result = int(1e9)

for bit in range(1 << n):
    tmp = [a[:] for a in arr]
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                tmp[i][j] = 'H' if tmp[i][j] == 'T' else 'T'

    tsum = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if tmp[j][i] == 'T':
                cnt += 1
        tsum += min(cnt, n - cnt)

    result = min(tsum, result)

print(result)