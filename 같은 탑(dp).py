import sys
import math
INF = int(1e9)
input = sys.stdin.readline
n = int(input())
height = list(map(int,input().split()))
dp = [[-1 for g in range(500002)] for i in range(n + 1)]
if n == 1:
  print(-1)
  sys.exit()
if n == 2:
  if height[0] == height[1]:
    print(height[0])
  else:
    print(-1)
  sys.exit()
for i in range(n, -1, -1):
  for j in range(500002):
    if j == 500001:
      dp[i][j] = -INF
    if i == n:
        if j == 0:
          dp[i][j]=0
        else:
          dp[i][j] = -INF
    else:
        dp[i][j] = max([dp[i + 1][j], dp[i + 1][min(500001, j + height[i])], dp[i + 1][abs(height[i] - j)] + min(height[i], j)])
ans = dp[0][0]
print(dp[0][0] if dp[0][0] != 0 else "-1")
