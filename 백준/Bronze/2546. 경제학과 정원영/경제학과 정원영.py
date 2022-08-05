import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
for _ in range(int(input())):
  input()
  n, m = map(int, input().split())
  a = sorted(list(map(int, input().split())))
  cnt = 0
  b = list(map(int, input().split()))
  suma = sum(a)
  sumb = sum(b)
  i = 0  
  for i in range(n):
    if suma / n < (suma - a[i]) / (n - 1) and sumb / m < (sumb + a[i]) / (m + 1):
      cnt += 1
    elif cnt > 0: break 
  print(cnt)