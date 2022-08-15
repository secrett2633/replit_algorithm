import sys
from itertools import product
input = sys.stdin.readline
for _ in range(int(input())):
  j, n = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(n)]
  cnt = []
  for a, b in arr:
    cnt.append(a * b)
  cnt.sort(reverse = True)
  res = 0
  while j > 0:
    j -= cnt.pop(0)
    res += 1
  print(res)