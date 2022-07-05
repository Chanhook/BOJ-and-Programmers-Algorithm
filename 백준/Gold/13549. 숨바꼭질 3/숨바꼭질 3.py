import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX=100001
arr = [-1]*MAX

if n > k :
    print(n-k)
    exit()

q = deque()

q.append(n)
arr[n] = 0

while q : 
    x = q.popleft()
    if x == k :
        print(arr[x])
        break
    if 0 <= x-1 < MAX and arr[x-1] == -1:
        q.append(x-1)
        arr[x-1] = arr[x] + 1
    if 0 <= x*2 < MAX and arr[x*2] == -1:
        q.append(x*2)
        arr[x*2] = arr[x]
    if 0 <= x+1 < MAX and arr[x+1] == -1:
        q.append(x+1)
        arr[x+1] = arr[x] + 1