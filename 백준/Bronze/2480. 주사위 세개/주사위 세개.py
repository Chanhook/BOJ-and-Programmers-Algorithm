import sys
from collections import Counter

eyes = map(int, sys.stdin.readline().split())
counter = Counter(eyes).most_common(3)
# print(counter)
if len(counter) == 1:
    print(10000 + counter[0][0] * 1000)
elif len(counter) == 2:
    print(1000 + counter[0][0] * 100)
elif len(counter) == 3:
    counter.sort()
    print(counter[-1][0] * 100)
