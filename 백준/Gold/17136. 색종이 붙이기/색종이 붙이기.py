import sys


def check(r, c, size):
    total_one = size**2
    for i in range(size):
        total_one -= sum(papers[r+i][c:c+size])

    if total_one == 0:
        return True
    return False


def recursive(one_cnt, color_paper_cnt):
    global answer

    # 현재 상태가 올바른 해인지 확인
    # papers 에 더이상 1이 없는 경우
    if not one_cnt:
        answer = min(answer, color_paper_cnt)
        return

    # 현재 상태가 올바르지 않을 경우
    # 남은 색종이 수가 하나도 없을 경우
    if sum(left) == 0:
        return
    # 아직 1을 다 채우기전 이미 색종이 사용 개수가
    # answer 보다 많은 경우
    if color_paper_cnt >= answer:
        return

    for r in range(10):
        for c in range(10):
            if papers[r][c] == 1:
                for size in [5, 4, 3, 2, 1]:
                    # 남은 색종이 개수와 색종이를 붙일 시 범위를 넘지 않는다
                    if left[size] and r+size <= 10 and c+size <= 10:
                        # 위의 색종이 크기로 1을 빠짐없이 덮을 수 있는 지 확인
                        if check(r, c, size):
                            # papers 상태 변경, 색종이 개수 하나 감소
                            for i in range(r, r+size):
                                for j in range(c, c+size):
                                    papers[i][j] = 0
                            left[size] -= 1

                            # 하위 트리 확인
                            recursive(one_cnt-size**2, color_paper_cnt+1)

                            # 이전 상태로 돌아가기, 색종이 개수 복원
                            for i in range(r, r+size):
                                for j in range(c, c+size):
                                    papers[i][j] = 1
                            left[size] += 1
                return


papers = []
left = [0]+[5]*5
answer = sys.maxsize
one_cnt = 0

for _ in range(10):
    line = list(map(int, sys.stdin.readline().split()))
    one_cnt += sum(line)
    papers.append(line)

recursive(one_cnt, 0)

if one_cnt == 0:
    print(0)
else:
    print(-1) if answer == sys.maxsize else print(answer)
