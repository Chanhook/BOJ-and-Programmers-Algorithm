import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

lis = [0 for i in range(n)]
lis[0] = arr[0]


def binary_search(start, end, target):
    while start < end:
        mid = (start + end) // 2
        if lis[mid] < target:
            start = mid + 1
        else:
            end = mid

    return end


pointer = 0
for i in range(1, n):
    if lis[pointer] < arr[i]:
        lis[pointer+1] = arr[i]
        pointer += 1
    else:
        idx = binary_search(0, pointer, arr[i])
        lis[idx] = arr[i]

print(len(lis)-lis.count(0))
