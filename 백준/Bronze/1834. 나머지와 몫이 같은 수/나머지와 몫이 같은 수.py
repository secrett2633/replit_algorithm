import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

n = int(input())
res = 0
for i in range(1, n):
  if i == (n * i + i) % n == (n * i + i) // n: res += (n * i + i)
print(res)