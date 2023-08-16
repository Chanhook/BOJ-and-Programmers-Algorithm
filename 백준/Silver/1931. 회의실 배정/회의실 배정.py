import sys

input = sys.stdin.readline
n = int(input().strip())
info = [list(map(int, input().split())) for _ in range(n)]
sorted_info = sorted(info, key=lambda x: (x[0], x[1]))

ans = 1
s, e = sorted_info[0]
for i in range(1, n):
    ns, ne = sorted_info[i]
    if ne < e:
        s, e = ns, ne
    elif ns >= e:
        s, e = ns, ne
        ans += 1

print(ans)
