from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    sum_q1 = sum(q1)
    q2 = deque(queue2)
    sum_q2 = sum(q2)
    total = sum_q1 + sum_q2
    limit = max(len(q1), len(q2)) * 4
    cnt = 0
    i = total // 2

    if sum_q1 == i:
        return 0

    while cnt < limit and sum_q1 != i:
        cnt += 1
        if sum_q1 > i:
            if len(q1) > 1:
                pl = q1.popleft()
                sum_q1 -= pl
                q2.append(pl)
            else:
                pl = q2.popleft()
                q1.append(pl)
                sum_q1 += pl
        else:
            if len(q2) > 1:
                pl = q2.popleft()
                q1.append(pl)
                sum_q1 += pl
            else:
                pl = q1.popleft()
                sum_q1 -= pl
                q2.append(pl)

    return -1 if sum_q1 != i else cnt