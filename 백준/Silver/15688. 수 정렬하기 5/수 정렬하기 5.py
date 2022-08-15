import sys
from itertools import combinations
import math
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)])
for i in arr:
  print(i)
