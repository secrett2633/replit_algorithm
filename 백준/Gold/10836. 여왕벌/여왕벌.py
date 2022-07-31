import sys
from collections import deque
import copy
import math
input = sys.stdin.readline  
m, n = map(int, input().split())
arr = [[1] * m for _ in range(m)]
graph = [0] * (2 * m - 1)
for _ in range(n):
  a, b, c = map(int, input().split())
  for i in range(a, a + b):
    graph[i] += 1
  for i in range(a + b, 2 * m - 1):
    graph[i] += 2    
cnt = 0
for j in range(m - 1, -1, -1):
  arr[j][0] += graph[cnt]
  cnt += 1
for j in range(1, m):
  arr[0][j] += graph[cnt]
  cnt += 1
for i in range(1, m):
  for j in range(1, m):
    arr[i][j] += arr[0][j] - 1
for i in range(m):
  print(" ".join(map(str, arr[i])))