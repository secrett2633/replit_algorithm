import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]      
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = 0
for rain in range(101):
  visited = [[False] * n for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j] and arr[i][j] >= rain:
        q = deque([[i, j]])
        while q:
          x, y = q.pop()
          if visited[x][y] or arr[x][y] < rain: continue
          visited[x][y] = True
          for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
              q.append([nx, ny])
        cnt += 1
  res = max(res, cnt)
print(res)
