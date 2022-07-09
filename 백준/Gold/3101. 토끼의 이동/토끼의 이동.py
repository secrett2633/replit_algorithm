import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = input().rstrip()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
nx = 1
ny = 1
res = 1
dp = [0] * (n * 2)
dp[1] = 1
d = {"U":0, "D":1, "L":2, "R":3}
for i in range(2, n * 2):
  if i - 1 <= n: tmp = i - 1
  else: tmp = n - (i - 1) % n
  dp[i] = dp[i - 1] + tmp
for i in s:
  nx += dx[d[i]]; ny += dy[d[i]]
  if nx + ny - 1 <= n:
    if (nx + ny - 1) % 2 == 0:
      res += dp[nx + ny - 1] + nx - 1
    else:
      res += dp[nx + ny - 1] + ny - 1
  else:
    if (nx + ny - 1) % 2 == 0:
      res += dp[nx + ny - 1] + n - ny
    else:
      res += dp[nx + ny - 1] + n - nx
print(res)