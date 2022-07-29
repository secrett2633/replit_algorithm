import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
n = int(input())
cnt = 0
for i in range(1, 1001):
  for j in range(1, i):
    if i ** 2 == j ** 2 + n: cnt += 1; break
print(cnt)