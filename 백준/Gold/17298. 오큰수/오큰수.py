import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
indices = [i for i in range(len(A))]

answer = [-1 for _ in range(len(A))]
stack = [indices[0]]

for i in range(1, len(A)):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
