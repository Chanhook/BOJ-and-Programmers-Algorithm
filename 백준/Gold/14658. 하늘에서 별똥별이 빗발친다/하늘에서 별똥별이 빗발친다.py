import sys

n, m, l, k = map(int, sys.stdin.readline().split())
star_loc = []

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    star_loc.append((x, y))

ans = -sys.maxsize
for i in range(k):
    for j in range(k):
        cnt = 0
        x = star_loc[i][0]
        y = star_loc[j][1]
        for c in range(k):
            cx = star_loc[c][0]
            cy = star_loc[c][1]
            if x <= cx <= x+l and y <= cy <= y+l:
                cnt += 1
        ans = max(ans, cnt)

print(k-ans)
