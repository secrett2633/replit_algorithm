import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

n, l, d = map(int, input().split())
now = 0
cache = [False] * (n * l + 5 * n)
for _ in range(n):
  for i in range(l):
    cache[now + i] = True
  now += (l + 5)
res = 0
while res < n * l + 5 * (n - 1):
  if not cache[res]: break
  res += d
print(res)