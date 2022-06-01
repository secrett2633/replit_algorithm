import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solve(x, y):
  if x == n - 1 and y == m - 1:
    return 1
  if dp[x][y] != -1:
    return dp[x][y]
  res = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if arr[nx][ny] < arr[x][y]:
        res += solve(nx, ny)
  dp[x][y] = res
  return dp[x][y]
solve(0, 0)
print(dp[0][0])