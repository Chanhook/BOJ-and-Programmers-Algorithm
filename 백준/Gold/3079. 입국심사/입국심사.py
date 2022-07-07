import sys

n, m = map(int, sys.stdin.readline().split())
times = []
for i in range(n):
    times.append(int(input()))
times.sort()


start = 1
end = times[-1] * m
result = times[-1] * m

while start <= end:
    mid = (start + end) // 2

    done_num = 0
    done_num = sum(mid // time for time in times)

    if done_num >= m:
        end = mid - 1
        result = min(result, mid)
    elif done_num < m:
        start = mid + 1

print(result)

"""
최소 최대를 무엇으로 하지
심사 시간

Mid 심사시간동안 몇명의 사람을 처리할 수 있을지 생각
done_num보다 많이 처리하면 end를 줄이고
그때 min(result, Mid) 값이 결과값
done_num보다 적게 처리하면 start를 늘린다s
"""
