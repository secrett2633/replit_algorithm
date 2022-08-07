import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
#print(ord("a") - 97) 
n, k, b = map(int, input().split())
arr = [1] * n
for i in range(b):
  arr[int(input()) - 1] = 0
now = sum(arr[:k])
res = now
for i in range(k, n):
  now += (arr[i] - arr[i - k])
  res = max(now, res)
print(k - res)