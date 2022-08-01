import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
a, b = input().rstrip().split()
res = 0
for i in a:
  for j in b:
    res += int(i) * int(j)
print(res)