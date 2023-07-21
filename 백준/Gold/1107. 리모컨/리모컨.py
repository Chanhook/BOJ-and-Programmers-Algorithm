import sys

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
broken = list(input().split()) if m != 0 else []

now = 100
channels = int(1e6)
min_count = 1e9


def find():
    global min_count
    if n == now:
        min_count = 0
        return

    if m == 0:
        min_count = min(len(str(n)), abs(n - now))  # 이거를 빼먹었다 바로 이동하거나, +,- 로 이동하거나
        return

    for i in range(channels):
        cond = False
        for broken_number in broken:
            if broken_number in str(i):
                cond = True
                break
        if cond:
            min_count = min(abs(n - now), min_count)
        else:
            min_count = min(len(str(i)) + abs(n - i), min_count)


find()
print(min_count)
