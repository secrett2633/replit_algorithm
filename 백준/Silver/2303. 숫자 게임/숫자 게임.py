import sys
from itertools import combinations
import math
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = [0] * n
for i in range(n):
  for k in combinations(arr[i], 3):
    res[i] = max(res[i], sum(k) % 10)
for i in range(n - 1, -1, -1):
  if res[i] == max(res): print(i + 1); break
  