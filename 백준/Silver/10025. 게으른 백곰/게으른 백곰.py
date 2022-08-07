import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
#print(ord("a") - 97) 
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
#arr.sort(key = lambda x:x[1])
dp = [0] * 1000001
for i, j in arr:
  dp[j] = i
res = sum(dp[:k * 2])
ans = res
for i in range(k * 2 + 1, 1000001):
  res = res - dp[i - (k * 2 + 1)] + dp[i]
  ans = max(res, ans)
print(ans)