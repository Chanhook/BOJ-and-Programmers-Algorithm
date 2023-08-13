import sys

input = sys.stdin.readline
n, k = map(int, input().split())
words = [set(input().strip()) for _ in range(n)]
ans = 0
learn = [0] * 26


def init():
    for a in 'antic':
        a_ = ord(a) - ord('a')
        learn[a_] = 1


def dfs(idx, k):
    if k == 0:
        global ans
        cnt = 0
        flag = True
        for word in words:
            flag = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    flag = False
                    break
            if flag:
                cnt += 1

        ans = max(cnt, ans)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, k - 1)
            learn[i] = 0


if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    init()
    k -= 5
    dfs(0, k)
    print(ans)
