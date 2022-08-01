import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(set([int(input()) for _ in range(n)]))
dp = [0] + [int(1e9)] * m
for _ in range(n):
  for i in arr:
    for j in range(m):
      if j + i > m: break
      dp[j + i] = min(dp[j + i], dp[j] + 1)
if dp[m] == int(1e9): dp[m] = -1
print(dp[m])