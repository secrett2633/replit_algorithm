import sys
#sys.setrecursionlimit(10 ** 8)
from collections import deque
import heapq
import math
input = sys.stdin.readline    
n = int(input())
dp = [0, 1, 2, 3, 5] + [0] * n
for i in range(4, n + 1):
  dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
print(dp[n])