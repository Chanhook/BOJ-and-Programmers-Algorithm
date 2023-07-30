from collections import deque

s = int(input())
q = deque()
q.append((1, 0))
visited = dict()
visited[(1, 0)] = 0

while q:
    now, clip = q.popleft()
    if now == s:
        print(visited[(now, clip)])
        break

    if now < 0 or now > s:
        continue

    if (now, now) not in visited:
        visited[(now, now)] = visited[(now, clip)] + 1
        q.append((now, now))
    if (now + clip, clip) not in visited:
        visited[(now + clip, clip)] = visited[(now, clip)] + 1
        q.append((now + clip, clip))
    if (now - 1, clip) not in visited:
        visited[(now - 1, clip)] = visited[(now, clip)] + 1
        q.append((now - 1, clip))