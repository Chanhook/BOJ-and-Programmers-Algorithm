import sys
sys.setrecursionlimit(10**9)

# 노드의 개수
n = int(sys.stdin.readline())

# 트리
Tree = [[] for _ in range(n+1)]
# 부모 노드 저장
Parents = [0 for _ in range(n+1)]
# 트리 구조 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

# print(Tree)


# 연결된 노드들부터 parents[i]의 부모가 없으면 부모 설정 해주고, DFS 돌린다.
def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i, tree, parents)


DFS(1, Tree, Parents)
for p in Parents[2:]:
    print(p)
