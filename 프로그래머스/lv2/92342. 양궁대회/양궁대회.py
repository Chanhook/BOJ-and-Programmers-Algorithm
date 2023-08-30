def solution(n, info):
    answer = []

    a_score = 0
    for i in range(len(info)):
        if info[i]:
            a_score += (10 - i)

    lion = [0] * 11
    max_diff = 0

    def dfs(left_arrow, target, a_score, l_score):
        if left_arrow < 0: return

        if left_arrow == 0 or target > 10:
            nonlocal max_diff, answer
            diff = l_score - a_score
            if diff > max_diff:
                if left_arrow:
                    lion[-1] += left_arrow
                max_diff = diff
                answer = lion[::]
            elif max_diff != 0 and diff == max_diff:
                if left_arrow:
                    lion[-1] += left_arrow

                for i in range(10, -1, -1):
                    if answer[i] > lion[i]:
                        break
                    elif answer[i] < lion[i]:
                        answer = lion[::]
                        break
            return

        for arrow in [info[target], -1]:
            lion[target] = arrow + 1
            score = 10 - target if arrow != -1 else 0
            if info[target] != 0:
                dfs(left_arrow - lion[target], target + 1, a_score - score, l_score + score)
            else:
                dfs(left_arrow - lion[target], target + 1, a_score, l_score + score)
            lion[target] = 0

    dfs(n, 0, a_score, 0)

    return answer if max_diff else [-1]
