import sys
input = sys.stdin.readline
dp = [[1] * 10] + [[0] * 10 for _ in range(65)]
for i in range(1, 65):
  for j in range(10):
    for k in range(j + 1):
      dp[i][j] += dp[i - 1][k]
t = int(input())
for _ in range(t):
  n = int(input())
  print(dp[n][9])