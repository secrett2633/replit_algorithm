import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solve(x, y):
  if dp[x][y] != -1:
    return dp[x][y] + 1
  dp[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if arr[nx][ny] > arr[x][y]:
        dp[x][y] = max(dp[x][y], solve(nx, ny))
  return dp[x][y] + 1
result = 0
for i in range(n):
  for j in range(n):
    result = max(result, solve(i, j))
print(result)