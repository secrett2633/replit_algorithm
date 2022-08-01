import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
n, q = map(int, input().split())
arr = [int(input()) for _ in range(n)]
for _ in range(q):
  t = int(input())
  now = -1
  for i in range(n):
    now += arr[i]
    if now >= t: print(i + 1); break