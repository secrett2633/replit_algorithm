import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

n = input().rstrip()
for i in range(len(n) - 1):
  a, b = 1, 1
  for j in n[:i + 1]:
    a *= int(j)
  for j in n[i + 1:]:
    b *= int(j)
  if a == b: print("YES"); break
else: print("NO")