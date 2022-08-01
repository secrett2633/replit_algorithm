import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for day in range(2001):
  visited = [[True] * n for _ in range(n)]
  tmp = []
  for i in range(n):
    for j in range(n):
      if not visited[i][j]: continue
      cache = [[i, j]]
      q = deque([[i, j]])
      while q:
        a, b = q.pop()
        for c in range(4):
          nx, ny = a + dx[c], b + dy[c]
          if [nx, ny] in cache: continue
          if not (0 <= nx < n and 0 <= ny < n): continue
          if not (l <= abs(arr[nx][ny] - arr[a][b]) <= r): continue
          q.append([nx, ny])
          cache.append([nx, ny])
      if len(cache) < 2: continue
      else: 
        for a, b in cache:
          visited[a][b] = False
        tmp.append(cache)
  for cache in tmp:
    cnt = 0
    for a, b in cache:
      cnt += arr[a][b]
    for a, b in cache:
      arr[a][b] = cnt // len(cache)
  if not tmp: print(day); break