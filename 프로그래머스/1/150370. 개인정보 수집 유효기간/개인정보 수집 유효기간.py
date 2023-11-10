def solution(today, terms, privacies):
    answer = []
    now_year, now_month, now_day = map(int, today.split('.'))
    now_day = now_year * 12 * 28 + (now_month - 1) * 28 + now_day

    contract_dic = dict()
    for t in terms:
        cate, term = t.split()
        term = int(term)
        contract_dic[cate] = term

    for i, p in enumerate(privacies):
        contract_date, cate = p.split()
        con_year, con_month, con_day = map(int, contract_date.split('.'))
        con_day = con_year * 12 * 28 + (con_month - 1) * 28 + con_day

        end_day = con_day + contract_dic[cate] * 28
        if end_day <= now_day:
            answer.append(i + 1)

    return answer