import sys

input = sys.stdin.readline
n = int(input().strip())
marbles = list(map(int, input().split()))
removed = [0] * n
max_energy = 0


def find_idx(del_idx):
    l, r = 0, 0
    for i in range(del_idx - 1, -1, -1):
        if not removed[i]:
            l = i
            break
    for i in range(del_idx + 1, n):
        if not removed[i]:
            r = i
            break

    return l, r


def find_max_energy(arr, del_idx, energy, left):
    if left == 2:
        global max_energy
        max_energy = max(energy, max_energy)
        return

    for i in range(1, n - 1):
        if not removed[i]:
            removed[i] = 1
            left_idx, right_idx = find_idx(i)
            find_max_energy(arr, i, energy + arr[left_idx] * arr[right_idx], left - 1)
            removed[i] = 0


for i in range(1, n - 1):
    removed[i] = 1
    find_max_energy(marbles, i, marbles[i - 1] * marbles[i + 1], n - 1)
    removed[i] = 0

print(max_energy)
