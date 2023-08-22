n = list(input())
n.sort(reverse=True)

if n[-1] != '0':
    print(-1)
else:
    s = sum(map(int, n))
    if s % 3 == 0:
        print(''.join(n))
    else:
        print(-1)
