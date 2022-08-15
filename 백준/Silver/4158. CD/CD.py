import sys
from itertools import permutations
import math
input = sys.stdin.readline
while True:
  n, m = map(int, input().split())
  if n == m == 0: break
  cache = {}
  res = 0
  for i in range(n):
    a = int(input())
    try:
      cache[a] += 1 
    except:
      cache[a] = 1
  for i in range(m):
    a = int(input())
    try:
      cache[a] -= 1 
      if cache[a] >= 0: res += 1
    except:
      continue
  print(res)