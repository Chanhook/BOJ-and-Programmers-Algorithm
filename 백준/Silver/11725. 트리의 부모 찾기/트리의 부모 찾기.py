import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for i in range(n-1):
    n1,n2 = map(int,input().split())
    tree[n1] += [n2]
    tree[n2] += [n1]


def dfs(start,tree,parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i,tree,parents)

dfs(1,tree,parents)
for p in parents[2:]:
    print(p)
    