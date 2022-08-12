import sys

n = int(sys.stdin.readline().strip())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()

l = 0
r = n-1
value = 2000000000

while l < r:
    x = solutions[l]+solutions[r]
    if x == 0:
        ll = l
        rr = r
        break
    else:
        if x < 0:
            if abs(x) < value:
                value = abs(x)
                ll = l
                rr = r
            l += 1
        elif x > 0:
            if abs(x) < value:
                value = abs(x)
                ll = l
                rr = r
            r -= 1

print(solutions[ll], solutions[rr])
