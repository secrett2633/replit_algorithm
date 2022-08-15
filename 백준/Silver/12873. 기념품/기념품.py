import sys
from itertools import permutations
import math
input = sys.stdin.readline
n = int(input())
arr = list(range(1, n + 1))
d = 1
now = 0
while len(arr) > 1:
  now = (now + d ** 3 - 1) % len(arr)
  del arr[now]
  d += 1
print(arr[0])