import sys
import copy
import heapq
import bisect
from itertools import combinations
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)
def dfs(use, now):
  if not use:
    global res
    tmp = arr[now[-1]][now[0]]
    if tmp == 0: return
    for i in range(1, n):
      if arr[now[i - 1]][now[i]] == 0: return
      tmp += arr[now[i - 1]][now[i]]
    res = min(res, tmp)      
  else:
    for i in use:
      tmp = use[::]
      tmp.remove(i)
      dfs(tmp, now + [i])
dfs(list(range(n)), [])
print(res)