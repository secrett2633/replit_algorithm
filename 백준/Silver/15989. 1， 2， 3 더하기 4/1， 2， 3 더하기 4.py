import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * (max(arr) + 1)
for v in [1, 2, 3]:
  if v <= max(arr): dp[v] += 1
  for i in range(v, max(arr) + 1):
    dp[i] += dp[i - v]
for i in arr:
  print(dp[i])
