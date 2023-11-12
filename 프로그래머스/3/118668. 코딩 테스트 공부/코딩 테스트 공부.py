def solution(alp, cop, problems):
    target_alp = target_cop = 0
    for p in problems:
        target_alp, target_cop = max(p[0], target_alp), max(p[1], target_cop)

    if target_alp <= alp and target_cop <= cop:
        return 0

    # 인덱스 에러
    # 타켓이 초기값보다 작은 경우 있음
    dp = [[float('inf')] * (target_cop + 1) for _ in range(target_alp + 1)]
    alp = min(target_alp, alp)
    cop = min(target_cop, cop)
    dp[alp][cop] = 0
    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            if i < target_alp:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            if j < target_cop:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, target_alp)
                    new_cop = min(j + cop_rwd, target_cop)
                    dp[new_alp][new_cop] = min(dp[i][j] + cost, dp[new_alp][new_cop])

    return dp[target_alp][target_cop]