from collections import deque


def solution(queue1, queue2):
    answer = -1
    length = len(queue1) + len(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    count = 0
    while count < length * 2:
        if s1 == s2:
            answer = count
            break
        while s1 < s2 and len(q2) > 1:
            popleft = q2.popleft()
            q1.append(popleft)
            s1 += popleft
            s2 -= popleft
            count += 1
        if s1 == s2:
            answer = count
            break
        while s1 < s2 and len(q1) > 1:
            popleft = q1.popleft()
            q2.append(popleft)
            s1 -= popleft
            s2 += popleft
            count += 1
        if s1 == s2:
            answer = count
            break
        while s2 < s1 and len(q1) > 1:
            popleft = q1.popleft()
            q2.append(popleft)
            s2 += popleft
            s1 -= popleft
            count += 1
        if s1 == s2:
            answer = count
            break
        while s2 < s1 and len(q2) > 1:
            popleft = q2.popleft()
            q1.append(popleft)
            s2 -= popleft
            s1 += popleft
            count += 1
        if s1 == s2:
            answer = count
            break
    return answer