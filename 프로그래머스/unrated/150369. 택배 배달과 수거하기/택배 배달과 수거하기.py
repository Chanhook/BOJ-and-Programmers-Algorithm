def solution(cap, n, deliveries, pickups):
    answer = 0
    deli_left = sum(deliveries)
    pick_left = sum(pickups)
    deli_idx = pick_idx = len(deliveries) - 1
    for i in range(len(deliveries) - 1, -1, -1):
        if deliveries[i] != 0:
            deli_idx = i
            break
    for i in range(len(pickups) - 1, -1, -1):
        if pickups[i] != 0:
            pick_idx = i
            break

    while deli_left > 0 or pick_left > 0:
        answer += max(deli_idx + 1, pick_idx + 1) * 2
        deli_cap = cap
        for i in range(deli_idx, -1, -1):
            if deliveries[i] - deli_cap > 0:
                deliveries[i] -= deli_cap
                deli_left -= deli_cap
                break
            else:
                deli_cap -= deliveries[i]
                deli_left -= deliveries[i]
                deli_idx -= 1
                deliveries[i] = 0

        pick_cap = cap
        for i in range(pick_idx, -1, -1):
            if pickups[i] - pick_cap > 0:
                pickups[i] -= pick_cap
                pick_left -= pick_cap
                break
            else:
                pick_cap -= pickups[i]
                pick_left -= pickups[i]
                pick_idx -= 1
                pickups[i] = 0

    return answer