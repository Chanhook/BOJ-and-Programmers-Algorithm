import sys

N = int(sys.stdin.readline().strip())
tops = list(map(int, sys.stdin.readline().split()))
indices = [i for i in range(len(tops))]

answer = [0 for _ in range(len(tops))]
stack = [indices[-1]]

for i in range(len(tops)-2,-1,-1):
    while stack and tops[stack[-1]] < tops[i]:
        answer[stack.pop()] = i+1
    stack.append(i)

print(*answer)
