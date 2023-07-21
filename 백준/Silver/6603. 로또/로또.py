import sys
from itertools import combinations

input = sys.stdin.readline


def find_lotto(k, nums):
    nums.sort()
    for p in combinations(nums, 6):
        print(*p)
    print()
    return


while True:
    tc = list(map(int, input().split()))
    if tc == [0]:
        break
    else:
        k, nums = tc[0], tc[1:]
        find_lotto(k, nums)
