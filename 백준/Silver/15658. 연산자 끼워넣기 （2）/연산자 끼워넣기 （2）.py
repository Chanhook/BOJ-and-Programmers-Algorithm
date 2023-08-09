n = int(input().strip())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_value = -int(1e10)
min_value = int(1e10)
used = [0] * n


def calc(i, now, num_idx):
    num = nums[num_idx]
    if i == 0:  # 더하기
        return now + num
    elif i == 1:
        return now - num
    elif i == 2:
        return now * num
    elif i == 3:
        if now < 0:
            return -(-1 * now // num)
        else:
            return now // num


def dfs(now, num_idx, operand_cnt):
    if operand_cnt == n - 1:
        global max_value, min_value
        max_value = max(now, max_value)
        min_value = min(now, min_value)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            calc_result = calc(i, now, num_idx + 1)
            dfs(calc_result, num_idx + 1, operand_cnt + 1)
            operators[i] += 1


dfs(nums[0], 0, 0)

print(max_value)
print(min_value)
