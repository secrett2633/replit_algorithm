import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
res = 0
arr = [0] + sorted(list(map(int, input().split())))
partial_sum = [0] * (n + 1)
for i in range(1, n + 1):
  partial_sum[i] = partial_sum[i-1] + arr[i]
for i in range(n):
  res += (partial_sum[i + 1] - partial_sum[i]) * (partial_sum[-1] - partial_sum[i + 1])
print(res)