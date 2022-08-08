import sys
from itertools import combinations
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
def dfs(use, now):
  if len(now) == m:
    print(*now)
    return
  else:
    for i in use:
      dfs(use, now + [i])
dfs(arr, [])