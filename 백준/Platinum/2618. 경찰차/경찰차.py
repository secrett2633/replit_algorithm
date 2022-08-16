import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
w = int(input())
s = [list(map(int, input().split())) for _ in range(w)]
dp = [[-1] * (w + 1) for _ in range(w + 1)]
s1 = [[1, 1]] + s[::]
s2 = [[n, n]] + s[::]

def dfs(p1, p2, n, w):
  if p1 == w or p2 == w: return 0
  if dp[p1][p2] != -1: return dp[p1][p2]
  cnt = max(p1,p2) + 1
  l1 = abs(s[cnt-1][0]-s1[p1][0]) + abs(s[cnt-1][1] - s1[p1][1])
  l2 = abs(s[cnt-1][0]-s2[p2][0]) + abs(s[cnt-1][1] - s2[p2][1])
  dp[p1][p2] = min(l1 + dfs(cnt, p2, n, w),l2 + dfs(p1, cnt, n, w))
  return dp[p1][p2]

def solve(p1,p2,w):
  if p1 == w or p2 == w: return
  cnt = max(p1, p2) + 1
  l1 = abs(s[cnt-1][0] - s1[p1][0]) + abs(s[cnt-1][1] - s1[p1][1])
  l2 = abs(s[cnt-1][0] - s2[p2][0]) + abs(s[cnt-1][1] - s2[p2][1])
  if l1 + dp[cnt][p2] < l2 + dp[p1][cnt]: print(1); solve(cnt, p2, w)
  else: print(2); solve(p1, cnt, w)
print(dfs(0, 0, n, w))
solve(0, 0, w)