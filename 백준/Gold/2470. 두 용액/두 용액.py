import re
import sys

n = int(sys.stdin.readline().strip())
solution = list(map(int, sys.stdin.readline().split()))
solution.sort()
answer = []
s, e = 0, n - 1
value = 2e9 + 1

while s < e:
    start = solution[s]
    end = solution[e]
    result = start + end
    if abs(result) < value:
        value = abs(result)
        answer = [start, end]

    if result < 0:
        s += 1
    else:
        e -= 1

print(*answer)
