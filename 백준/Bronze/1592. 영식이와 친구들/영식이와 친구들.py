import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
n, m, l = map(int, input().split())
arr = [0] * n
arr[0] = 1
now = 0
for i in range(10000):
  if arr[now] == m: print(i); break
  if arr[now] % 2 == 1: now = (now + l) % n
  else: now = (now - l + n) % n
  arr[now] += 1