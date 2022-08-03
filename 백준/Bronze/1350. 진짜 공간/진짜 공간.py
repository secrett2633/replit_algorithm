import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
d = int(input())
res = 0
for i in arr:
  try:
    res += math.ceil(i / d)
  except:
    continue
print(res * d)