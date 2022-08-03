import sys
from collections import deque, Counter
import copy
from queue import PriorityQueue
input = sys.stdin.readline
N, m, M, T, R = map(int, input().split())
now = m
cnt = 0
res = 0
while cnt < N:
  res += 1
  if cnt == 0 and res == 1000000: print(-1); break
  if now + T <= M: cnt += 1; now += T
  else: now = max(now - R, m)
else: print(res)