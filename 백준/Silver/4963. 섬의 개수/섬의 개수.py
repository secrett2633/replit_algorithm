import sys
import copy
import heapq
import bisect
from itertools import combinations
from collections import deque
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
while True:
  w, h = map(int, input().split())
  if w == h == 0: break
  cnt = 0
  arr = [list(map(int, input().split())) for _ in range(h)]
  visited = [[False] * w for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if not visited[i][j] and arr[i][j] == 1:
        q = deque([[i, j]])
        while q:
          x, y = q.pop()
          if not visited[x][y] and arr[x][y] == 1:
            visited[x][y] = True
            for k in range(8):
              nx, ny = x + dx[k], y + dy[k]
              if not (0 <= nx < h) or not (0 <= ny < w) or arr[nx][ny] == 0: continue
              q.append([nx, ny])
        cnt += 1
  print(cnt)