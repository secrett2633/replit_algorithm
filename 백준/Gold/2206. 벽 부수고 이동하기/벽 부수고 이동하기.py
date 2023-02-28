from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, (input().split()))
graph = []
for i in range(n):
  graph.append(list(map(int, input().rstrip())))
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]
def bfs(x, y):
  q = deque()
  visited[0][0][0] = 1
  q.append((x, y, 0))
  while q:
    x, y, cnt = q.popleft()
    if x == n - 1 and y == m - 1:
      return visited[x][y][cnt]
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx <0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 1 and cnt == 0:
        visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
        q.append((nx, ny, cnt + 1))
      elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
        visited[nx][ny][cnt] = visited[x][y][cnt] + 1
        q.append((nx, ny, cnt))
  return -1

print(bfs(0, 0))
    