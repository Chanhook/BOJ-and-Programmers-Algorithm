import math
n, k=map(int, input().split())
numbers=[]
cnt=0
left=0

for i in range(n):
    a=int(input())
    numbers.append(a)


for num in reversed(numbers):
    if(num>k):
        continue
    else:
        cnt+=math.floor(k/num)
        k=k%num
print(cnt)
