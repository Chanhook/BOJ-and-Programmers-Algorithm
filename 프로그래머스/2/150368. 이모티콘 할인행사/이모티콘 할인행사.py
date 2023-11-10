def solution(users, emoticons):
    answer = []

    user_dic = {}
    for i, user in enumerate(users):
        user_dic[i] = user

    discount = [0] * len(emoticons)

    def dfs(idx):
        if idx == len(emoticons):
            result = [0, 0]
            for user in range(len(users)):
                ratio, budget, = user_dic[user]
                purchase = 0
                for e, d in zip(emoticons, discount):
                    if d >= ratio:
                        purchase += e * (100 - d) // 100
                    else:
                        continue

                if purchase >= budget:
                    result[0] += 1
                else:
                    result[1] += purchase
            answer.append(result)
            return

        for d in [40, 30, 20, 10]:
            discount[idx] += d
            dfs(idx + 1)
            discount[idx] -= d

    dfs(0)
    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]