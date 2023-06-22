def solution(today, terms, privacies):
    answer = []
    
    now_year, now_month, now_day = map(int, today.split('.'))
    now_time = (now_day + now_month*28 + now_year*12*28)
    
    terms_dic = dict()
    for term in terms:
        t, m = term.split(' ')
        terms_dic[t] = m
    
    for i, privacy in enumerate(privacies):
        date, t = privacy.split(' ')
        pri_year, pri_month, pri_day = map(int, date.split('.'))
        pri_time = (pri_day + pri_month*28 + pri_year*12*28)
        term = int(terms_dic[t]) * 28

        if pri_time + term <= now_time:
            answer.append(i+1)
    
    return answer