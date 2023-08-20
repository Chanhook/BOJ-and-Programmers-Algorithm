import heapq

n = int(input().strip())
positive_heap = []
zero = []
negative_heap = []
for _ in range(n):
    num = int(input().strip())
    if num > 0:
        heapq.heappush(positive_heap, -1 * num)
    elif num == 0:
        zero.append(num)
    else:
        heapq.heappush(negative_heap, num)

ph_size = len(positive_heap)
nh_size = len(negative_heap)

result = 0
for i in range(0, ph_size, 2):
    if i == ph_size - 1 and len(positive_heap) == 1:
        break

    n1 = -1 * heapq.heappop(positive_heap)
    n2 = -1 * heapq.heappop(positive_heap)
    result += n1 * n2 if n1 != 1 and n2 != 1 else n1 + n2

for i in range(0, nh_size, 2):
    if i == nh_size - 1 and len(negative_heap) == 1:
        break

    n1 = heapq.heappop(negative_heap)
    n2 = heapq.heappop(negative_heap)
    result += n1 * n2

if zero:
    result += -1 * heapq.heappop(positive_heap) if positive_heap else 0
else:
    result += -1 * heapq.heappop(positive_heap) if positive_heap else 0
    result += heapq.heappop(negative_heap) if negative_heap else 0

print(result)
