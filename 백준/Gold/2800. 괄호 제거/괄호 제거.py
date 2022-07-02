import sys
from itertools import combinations as C

exp = list(sys.stdin.readline().strip())

e = []
pair_idx = []
result = set()

for i, v in enumerate(exp):
    if v == "(":
        exp[i] = ""
        e.append(i)
    elif v == ")":
        exp[i] = ""
        pair_idx.append([e.pop(), i])

for i in range(len(pair_idx)):
    for j in C(pair_idx, i):
        Exp = exp.copy()
        for s, e in j:
            Exp[s] = "("
            Exp[e] = ")"
        result.add("".join(Exp))

print(*sorted(result), sep="\n")
"""
괄호들의 인덱스를 알기위해 스택을 사용
기존 괄호 위치를 ''로 없애놓고
콤비네이션으로 위치에 다시 괄호 넣기!
"""
