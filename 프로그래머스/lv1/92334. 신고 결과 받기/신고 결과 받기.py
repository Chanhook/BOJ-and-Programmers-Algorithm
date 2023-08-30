def solution(id_list, report, k):
    answer = {id: 0 for id in id_list}
    reporting = {id: set() for id in id_list}
    reported = {id: set() for id in id_list}

    for r in report:
        reporting_man, reported_man = r.split()
        reporting[reporting_man].add(reported_man)
        reported[reported_man].add(reporting_man)

    for id in id_list:
        if len(reported[id]) >= k:
            for reporter in reported[id]:
                answer[reporter] += 1

    return [v for v in answer.values()]