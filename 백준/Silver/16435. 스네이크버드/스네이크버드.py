import sys
from itertools import product
input = sys.stdin.readline
n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))
for i in arr:
  if i <= l: l += 1
print(l)
