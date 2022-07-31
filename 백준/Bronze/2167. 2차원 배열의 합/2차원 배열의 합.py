import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(int(input())):
  i, j, x, y = map(int, input().split())
  res = 0
  for a in range(i - 1, x):
    for b in range(j - 1, y):
      res += arr[a][b]
  print(res)