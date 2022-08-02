import sys
from collections import deque, Counter
import copy
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr = Counter(arr)
res = -1
if 0 not in arr: res = 0
for a, b in arr.items():
  if a == b: res = max(res, a)
print(res)