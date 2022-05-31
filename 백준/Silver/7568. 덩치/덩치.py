import sys

N = int(sys.stdin.readline().strip())

people_lst = []
for i in range(N):
    w, k = map(int, sys.stdin.readline().split())
    people_lst.append((w, k))

rank_dic = dict()
for i, (w, k) in enumerate(people_lst):
    temp = 1
    for j, (cp_w, cp_k) in enumerate(people_lst):
        if i == j:
            continue
        if w < cp_w and k < cp_k:
            temp += 1
    rank_dic[(w, k)] = temp

for people in people_lst:
    print(rank_dic[people],end=' ')