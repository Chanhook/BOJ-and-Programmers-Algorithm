import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

lis = [0 for i in range(n)]
lis[0] = arr[0]


def Binary_search(left, right, target):
    while left < right:
        mid = (left + right)//2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


pointer = 0
for i in range(1, n):
    if lis[pointer] < arr[i]:
        lis[pointer+1] = arr[i]
        pointer += 1
    else:
        idx = Binary_search(left=0, right=pointer, target=arr[i])
        lis[idx] = arr[i]


print(len(lis)-lis.count(0))
