from collections import defaultdict
from itertools import product


def solution(info, query):
    answer = []
    application_dic = defaultdict(list)

    for app in info:
        split = app.split()
        lang = ['-', split[0]]
        job = ['-', split[1]]
        career = ['-', split[2]]
        food = ['-', split[3]]
        score = int(split[4])
        for p in product(lang, job, career, food):
            application_dic[p] += [score]

    for k in application_dic.keys():
        application_dic[k].sort()

    for q in query:
        q = q.replace(' and ', ' ')
        q_split = q.split()
        key = tuple(q_split[:-1])
        score = int(q_split[-1])
        lo, hi = 0, len(application_dic[key])
        while lo < hi:
            mid = (lo + hi) // 2
            if application_dic[key][mid] < score:
                lo = mid + 1
            else:
                hi = mid
        answer.append(len(application_dic[key]) - lo)

    return answer
