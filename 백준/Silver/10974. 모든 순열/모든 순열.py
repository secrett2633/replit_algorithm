import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
def dfs(use, used, now):
  if not use: print(*now); return
  for i in use:
    tmp = use[::]
    tmp.remove(i)
    dfs(tmp, used + [i], now + [i])
dfs(list(range(1, n + 1)), [], [])