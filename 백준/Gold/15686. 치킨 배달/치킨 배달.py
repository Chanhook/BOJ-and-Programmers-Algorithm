'''
1초
- 보통 연산 횟수 10억 미만으로
- N의 범위 확인
  - 최대 50
  - 500 보다 작으므로 O(n^3) 으로 가능
512MB
- 리스트의 크기가 1,000만 단위 이상인가?
'''
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

chicken_loc = []
house_loc = []

answer=100000000

city = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for idx, r in enumerate(row):
        if r == 1:
            house_loc += [(i, idx)]
        elif r == 2:
            chicken_loc += [(i, idx)]
    city += [row]

for chicken in combinations(chicken_loc,m):
    temp=0
    for house in house_loc:
        dsts=[]
        for chick in chicken: 
            dst = abs(chick[0]-house[0]) + abs(chick[1]-house[1])
            dsts += [dst]
        temp += min(dsts)
    answer = min(answer,temp)

print(answer)