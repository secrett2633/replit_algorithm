import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0] * (k + 1)
for _ in range(n):
  v = int(input())
  if v <= k: dp[v] += 1
  for i in range(v, k + 1):
    dp[i] += dp[i - v]
print(dp[-1])
