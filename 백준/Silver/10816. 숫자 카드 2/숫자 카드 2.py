import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
num_cards = list(map(int, input().split()))
m = int(input())
check_cards = list(map(int, input().split()))

num_card_dic = defaultdict(int)
for num_card in num_cards:
    num_card_dic[num_card] += 1

for check_card in check_cards:
    print(num_card_dic[check_card], end=' ')
