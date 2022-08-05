import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
for _ in range(int(input())):
  v, e = map(int, input().split())
  flag = True
  graph = {i:[] for i in range(1, v + 1)}
  for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  visited = [[False, ""] for _ in range(v + 1)]
  for i in range(1, v + 1):
    if not visited[i][0]:
      q = deque([[i, True]])
      while q:
        x, y = q.pop()
        visited[x][0] = True
        visited[x][1] = y
        for k in graph[x]:
          if visited[k][0] and visited[k][1] == visited[x][1]: flag = False; break
          if not visited[k][0]: q.append([k, not y])
  if flag: print("YES")
  else: print("NO") 