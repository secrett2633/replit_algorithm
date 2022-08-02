import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
for _ in range(100000000):
  n = int(input())
  if n == 0: break
  arr = []
  for _ in range(n):
    a = input().rstrip()
    arr.append([a.lower(), a])
  arr.sort(key = lambda x:x[0])
  print(arr[0][1])