import sys
import copy
import heapq
import bisect
from itertools import combinations
input = sys.stdin.readline
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
now = sum(arr[:k])
res = now
for i in range(k, n):
  now = now - arr[i - k] + arr[i]
  res = max(res, now)
print(res)