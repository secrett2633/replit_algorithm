import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(set([int(input()) for _ in range(n)]))
dp = [0] * (100001)
for i in arr:
  dp[i] += 1
  for j in range(m):
    if j + i > m: break
    dp[j + i] += dp[j]
if dp[m] == int(1e9): dp[m] = -1
print(dp[m])