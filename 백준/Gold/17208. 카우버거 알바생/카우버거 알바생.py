import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (301) for _ in range(301)]
for a, b in query:
  tmp = []
  for i in range(301):
    for j in range(301):
      if i + a > m or j + b > k: break
      if dp[i][j] != 0: tmp.append([i, j, dp[i][j]])
  for i, j, r in tmp:
    dp[i + a][j + b] = max(dp[i + a][j + b], r + 1)
  dp[a][b] = max(dp[a][b], 1)
res = 0
for i in range(m + 1):
  for j in range(k + 1):
    res = max(res, dp[i][j])
print(res)