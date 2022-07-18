import sys
input = sys.stdin.readline
n, m, c0, d0 = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]
dp = [0] * (n + 1)
for i in range(n):
  if i + c0 > n: break
  dp[i + c0] = max(dp[i + c0], dp[i] + d0)
for a, b, c, d in query:
  for _ in range(a // b):
    tmp = []
    for i in range(n):
      if i + c > n: break
      tmp.append([i + c, dp[i] + d])
    for i, j in tmp:
      dp[i] = max(dp[i], j)
print(max(dp))