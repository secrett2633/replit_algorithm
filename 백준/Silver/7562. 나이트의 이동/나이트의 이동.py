import sys
from collections import deque
input = sys.stdin.readline     
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
for _ in range(int(input())):
  n = int(input())
  t1 = list(map(int, input().split()))
  t2 = list(map(int, input().split()))
  visited = [[0] * n for _ in range(n)]
  q = deque()
  q.append([t1[0], t1[1]])
  visited[t1[0]][t1[1]] = 1
  while q:
    x, y = q.popleft()
    if [x, y] == t2: break
    for i in range(8):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        q.append([nx, ny])
        visited[nx][ny] = visited[x][y] + 1
  print(visited[t2[0]][t2[1]] - 1)