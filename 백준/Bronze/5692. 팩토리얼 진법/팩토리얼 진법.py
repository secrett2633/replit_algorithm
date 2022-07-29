import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

while True:
  n = input().rstrip()[::-1]
  if n == "0": break
  res = 0
  for i, n in enumerate(n):
    res += (math.factorial(i + 1) * int(n))
  print(res)