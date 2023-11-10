def solution(cap, n, deliveries, pickups):
    answer = 0

    d_idx = n
    for d in deliveries[::-1]:
        if d != 0:
            break
        else:
            d_idx -= 1

    p_idx = n
    for p in pickups[::-1]:
        if p != 0:
            break
        else:
            p_idx -= 1

    deliveries = [0] + deliveries
    pickups = [0] + pickups

    while d_idx or p_idx:
        answer += (max(d_idx, p_idx)) * 2
        d_cap = cap
        while d_idx:
            if deliveries[d_idx] == 0:
                d_idx -= 1
                continue

            if d_cap == 0:
                break

            if deliveries[d_idx] - d_cap > 0:
                deliveries[d_idx] -= d_cap
                d_cap = 0
            else:
                d_cap -= deliveries[d_idx]
                deliveries[d_idx] = 0
                d_idx -= 1

        p_cap = cap
        while p_idx:
            if pickups[p_idx] == 0:
                p_idx -= 1
                continue

            if p_cap == 0:
                break

            if pickups[p_idx] - p_cap > 0:
                pickups[p_idx] -= p_cap
                p_cap = 0
            else:
                p_cap -= pickups[p_idx]
                pickups[p_idx] = 0
                p_idx -= 1

    return answer