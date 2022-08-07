import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
#print(ord("a") - 97) 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
now = sum(arr[:m])
res = now
for i in range(m, n):
  now += (arr[i] - arr[i - m])
  res = max(now, res)
print(res)