import sys
import copy
import heapq
import bisect
from itertools import combinations
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = -int(1e9)
def dfs(use, now):
  if not use:
    global result
    tmp = 0
    for i in range(n - 1):
      tmp += max(abs(now[i] - now[i + 1]), abs(now[i + 1] - now[i]))
    result = max(result, tmp)
  else:
    for i in use[::]:
      use.remove(i)
      dfs(use, now + [i])
      use.append(i)
dfs(arr, [])
print(result)