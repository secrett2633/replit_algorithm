import sys
from math import gcd
input = sys.stdin.readline
a, b = map(int, input().split())
n = int(input())
arr = sorted([int(input()) for _ in range(n)])
res = abs(a - b)
for i in arr:
  res = min(res, abs(i - b) + 1)
print(res)

