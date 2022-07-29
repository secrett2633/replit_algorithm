import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

while True:
  n = int(input())
  if n == 0: break
  res = 0
  for i in range(n):
    res += ((n - i) ** 2)
  print(res)