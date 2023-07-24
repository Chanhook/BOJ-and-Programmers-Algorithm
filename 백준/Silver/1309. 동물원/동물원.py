import sys

input = sys.stdin.readline
n = int(input().strip())
void, left, right = 1, 1, 1

for i in range(2, n + 1):
    new_void = void + left + right
    new_left = void + right
    new_right = void + left

    void, left, right = new_void, new_left, new_right

print((void + left + right) % 9901)
