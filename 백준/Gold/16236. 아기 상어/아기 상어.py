import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

for i in range(n):
  for j in range(n):
    if arr[i][j] == 9:
      now = [2, i, j]
      arr[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
  visited = [[-1] * n for i in range(n)]
  queue = deque([(now[1], now[2])])
  visited[now[1]][now[2]] = 0
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny < n and ny >= 0 and visited[nx][ny] == -1 and arr[nx][ny] <= now[0]:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))
  return visited

def fish(visit):
  x, y = 0, 0
  result = 1e9
  for i in range(n):
    for j in range(n):
      if visit[i][j] != -1 and arr[i][j] > 0 and arr[i][j] < now[0]:
        if visit[i][j] < result:
          x, y = i, j
          result = visit[i][j]
  if result == 1e9:
    return False
  else:
    now[1], now[2] = x, y
    return result

second = 0
cnt = 0

while True:
  value = fish(bfs())
  if value == False:
    print(second)
    break
  else:
    second += value
  arr[now[1]][now[2]] = 0
  cnt += 1
  if cnt >= now[0]:
    now[0] += 1
    cnt = 0
        