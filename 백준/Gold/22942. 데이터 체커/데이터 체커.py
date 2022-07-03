import sys

N = int(sys.stdin.readline().strip())
stack = []
circle = []

for i in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    a = inp[0] - inp[1]
    b = inp[0] + inp[1]
    circle.append([a, i, 0])
    circle.append([b, i, 1])
circle.sort(key=lambda x: (x[0], x[1]))

stack.append(circle[0])


def check(stack, circle):
    for i in range(1, len(circle)):
        if stack and stack[-1][2] == circle[i][2]:
            stack.append(circle[i])
        elif stack and stack[-1][2] != circle[i][2]:
            if stack[-1][1] == circle[i][1]:
                stack.pop()
            else:
                return print("NO")
        else:
            stack.append(circle[i])
    return print("YES")


check(stack, circle)
