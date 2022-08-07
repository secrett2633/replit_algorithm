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
res = [now, 1]
for i in range(m, n):
  now += (arr[i] - arr[i - m])
  if res[0] == now: res[1] += 1
  elif res[0] < now: res = [now, 1]
if res[0] > 0: print(res[0]); print(res[1])
else: print("SAD")