from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    
    report_id_dic=defaultdict(set)
    report_cnt_dic=defaultdict(int)
    
    send_dic=defaultdict(set)
    
    for string in report:
        user, reported = string.split(" ")
        l = len(report_id_dic[user])
        report_id_dic[user].add(reported)
        send_dic[reported].add(user)
        if l != len(report_id_dic[user]):
            report_cnt_dic[reported] += 1
    
    # print(report_id_dic)
    # print(report_cnt_dic)
    
    # print(send_dic)
    
    answer_dic = defaultdict(int)
    for user in id_list:
        report_cnt = report_cnt_dic[user]
        if report_cnt >= k:
            for send_user in send_dic[user]:
                answer_dic[send_user] += 1
    
    # print(answer_dic)
    
    for user in id_list:
        answer.append(answer_dic[user])
    
    return answer