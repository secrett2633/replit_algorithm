import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
a = 0
b = 0
for i in range(n):
  flag1 = False
  flag2 = False
  for j in range(n - 1):
    if arr[i][j] == arr[i][j + 1] == ".": flag1 = True
    elif flag1: a += 1; flag1 = False
    if arr[j][i] == arr[j + 1][i] == ".": flag2 = True
    elif flag2: b += 1; flag2 = False
  if flag1: a += 1
  if flag2: b += 1
print(a, b)
    