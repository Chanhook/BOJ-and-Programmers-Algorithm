from collections import deque
import heapq
import sys

n = int(sys.stdin.readline().strip())
classroom = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    classroom.append([s, t])
classroom.sort(key=lambda x: (x[0], x[1]))

q = deque(classroom)
heap = []
heapq.heappush(heap, q.popleft()[1])

while q:
    s, t = q.popleft()
    early_end_time = heapq.heappop(heap)
    if s < early_end_time:
        heapq.heappush(heap, early_end_time)
    heapq.heappush(heap, t)

print(len(heap))
