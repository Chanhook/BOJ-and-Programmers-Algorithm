import heapq


def solution(users, emoticons):
    answer = []
    emo_sale = [0] * len(emoticons)

    def dfs(idx, users):
        if idx < 0:
            heap = [0, 0]
            for user in users:
                total = 0
                for i in range(len(emo_sale)):
                    if user[0] <= emo_sale[i]:
                        total += emoticons[i] - (emoticons[i] * emo_sale[i] // 100)
                if total >= user[1]:
                    heap[0] += 1
                else:
                    heap[1] += total
            heapq.heappush(answer, (-heap[0], -heap[1]))
            return

        for sale in [40, 30, 20, 10]:
            emo_sale[idx] = sale
            dfs(idx - 1, users)

    dfs(len(emoticons) - 1, users)
    register, sales = heapq.heappop(answer)
    return [-register, -sales]