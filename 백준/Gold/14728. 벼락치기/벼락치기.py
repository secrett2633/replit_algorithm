import sys
input = sys.stdin.readline
n, t = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(n)]
query.sort()
dp = [0] * (10001)
for a, b in query:
  tmp = []
  for i in range(t):
    if i + a > t: break
    if dp[i] != 0: tmp.append([i + a, dp[i] + b])
  for i, j in tmp:
    dp[i] = max(dp[i], j)
  dp[a] = max(dp[a], b)
print(max(dp[:t+1]))