def solution(today, terms, privacies):
    answer = []
    now_year, now_month, now_day = map(int, today.split('.'))
    now = now_year * 12 * 28 + now_month * 28 + now_day
    expire_period = dict()
    for term in terms:
        cate, period = term.split()
        expire_period[cate] = int(period)

    for idx, privacy in enumerate(privacies):
        collected_date, cate = privacy.split()
        year, month, day = map(int, collected_date.split('.'))
        period = expire_period[cate]
        past = year * 12 * 28 + month * 28 + day

        if now >= past + period * 28:
            answer.append(idx+1)

    return answer
