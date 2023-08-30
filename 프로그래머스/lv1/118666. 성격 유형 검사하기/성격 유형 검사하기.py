def solution(survey, choices):
    answer = ''
    l = len(survey)

    score = [[0] * 2 for _ in range(4)]
    type_score_dic = {
        "RT": (0, 0),
        "TR": (0, 1),
        "CF": (1, 0),
        "FC": (1, 1),
        "JM": (2, 0),
        "MJ": (2, 1),
        "AN": (3, 0),
        "NA": (3, 1)
    }

    for i in range(l):
        s = survey[i]
        type, pos = type_score_dic[s]
        c = choices[i]
        if pos == 0:
            if c < 4:
                score[type][0] += 4 - c
            elif c > 4:
                score[type][1] += c - 4
        else:
            if c < 4:
                score[type][1] += 4 - c
            elif c > 4:
                score[type][0] += c - 4

    i = 0
    for t in ["RT", "CF", "JM", "AN"]:
        a, b = score[i]
        if a >= b:
            answer += t[0]
        else:
            answer += t[1]
        i += 1

    return answer