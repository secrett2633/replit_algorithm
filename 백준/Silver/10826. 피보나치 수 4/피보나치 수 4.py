import sys
from itertools import product
input = sys.stdin.readline
n = int(input())
dp = [0, 1, 1, 2] + [0] * n
for i in range(4, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])