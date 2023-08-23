import sys

input = sys.stdin.readline
n = int(input())
num_cards = set(map(int, input().split()))
m = int(input())
check_cards = list(map(int, input().split()))

for check_card in check_cards:
    if check_card in num_cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
