N, K = map(int, input().split())
if N >= K:
    print(0)
    exit()

elec_list = list(map(int, input().split()))

plug = set()
cnt = 0


def find_last(idx):
    result = 0
    max_idx = -1
    for num in plug:
        num_idx = K
        for i in range(idx, K):
            if elec_list[i] == num:
                num_idx = i
                break

        if max_idx < num_idx:
            result, max_idx = num, num_idx

    return result


for idx, num in enumerate(elec_list):
    plug.add(num)
    if len(plug) > N:
        cnt += 1
        latest_used = find_last(idx)
        plug.remove(latest_used)

print(cnt)
