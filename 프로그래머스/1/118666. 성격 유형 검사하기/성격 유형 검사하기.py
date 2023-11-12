def solution(survey, choices):
    answer = []

    table = [[0] * 2 for _ in range(4)]
    dic = {
        'RT': 0, 'TR': 0, 'R': 0, 'T': 1,
        'CF': 1, 'FC': 1, 'C': 0, 'F': 1,
        'JM': 2, 'MJ': 2, 'J': 0, 'M': 1,
        'AN': 3, 'NA': 3, 'A': 0, 'N': 1,
        0: 'RT', 1: 'CF', 2: 'JM', 3: 'AN'
    }
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    for s, c in zip(survey, choices):
        if c < 4:
            table[dic[s]][dic[s[0]]] += score[c]
        elif c > 4:
            table[dic[s]][dic[s[1]]] += score[c]

    for i, t in enumerate(table):
        personality = dic[i]
        if t[0] >= t[1]:
            answer.append(personality[0])
        else:
            answer.append(personality[1])
    return ''.join(answer)