def solution(alp, cop, problems):
    n = m = 0
    r = c = int(1e9)
    for a, b, _, _, _ in problems:
        n = max(n, a); m = max(m, b); r = min(r, a); c = min(c, b)
    dp = [[max(0, i - alp) + max(0, j - cop) for j in range(m + 1)] for i in range(n + 1)]
    for i in range(min(alp, n), n + 1):
        for j in range(min(cop, m), m + 1):            
            for x, y, dx, dy, cost in problems:
                if i - x >= 0 and j - y >= 0:
                    nx, ny = min(i + dx, n), min(j + dy, m)
                    dp[nx][ny] = min(dp[nx][ny], dp[i][j] + cost)
    return dp[n][m]