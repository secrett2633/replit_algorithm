import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def dfs(arr, now, n):
  if len(now) == 6:
    print(*now)
    return
  elif len(now) > 6: return
  for i in range(n, k):
    dfs(arr, now + [arr[i]], i + 1)
while True:
  k, *arr = map(int, input().split())
  if k == 0: break
  dfs(arr, [], 0)
  print()