from collections import defaultdict
from itertools import combinations as C


def solution(orders: list, course: list):
    answer = []

    combi_menu_cnt = defaultdict(int)

    for order in orders:
        len_order = len(order)
        for i in range(2, len_order + 1):
            for combi in C(list(order), i):
                menu = ''.join(sorted(list(combi)))
                combi_menu_cnt[menu] += 1

    for menu_cnt in course:
        max_menu = []
        max_menu_cnt = 0
        for menu, order_cnt in combi_menu_cnt.items():
            if len(menu) == menu_cnt and order_cnt >= 2:
                if order_cnt > max_menu_cnt:
                    max_menu.clear()
                    max_menu.append(menu)
                    max_menu_cnt = order_cnt
                elif order_cnt == max_menu_cnt:
                    max_menu.append(menu)
        answer += max_menu
    
    answer.sort()
    return answer
