import sys
#sys.setrecursionlimit(10 ** 8)
from collections import deque
import heapq
import math
input = sys.stdin.readline    
n = int(input())
dp = [0, 1, 1] + [0] * n
for i in range(3, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])