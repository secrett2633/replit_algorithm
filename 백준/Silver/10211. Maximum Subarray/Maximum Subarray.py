import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  res = -int(1e9)
  for i in range(1, n + 1):
    now = sum(arr[:i]) 
    res = max(res, now)
    for j in range(i, n):
      now = now - arr[j - i] + arr[j]
      res = max(res, now)    
  print(res)