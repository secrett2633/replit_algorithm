import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(set(list(map(int, input().split())))))
def dfs(now):
  if len(now) == m:
    print(*now)
  else:
    for i in arr:
      dfs(now + [i])
dfs([])