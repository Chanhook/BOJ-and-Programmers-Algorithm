import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input().strip())
words = []
weight = defaultdict(int)
word_to_num = dict()
ans = 0

for _ in range(n):
    w = list(input().strip())
    words.append(w)
    for i in range(len(w) - 1, -1, -1):
        weight[w[i]] += 10 ** (len(w) - i)

weights = sorted(weight.items(), key=lambda x: x[1], reverse=True)
# print(weights)

rank = 9
for alp, w in weights:
    word_to_num[alp] = str(rank)
    rank -= 1

for word in words:
    temp = ''
    for w in word:
        temp += word_to_num[w]
    ans += int(temp)

print(ans)