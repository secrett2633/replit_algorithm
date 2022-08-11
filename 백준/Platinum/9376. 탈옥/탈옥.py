from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
  visited = [[-1] * (w + 2) for _ in range(h + 2)]    
  q = deque()
  q.append([x,y])
  visited[x][y] = 0
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0 <= nx < h + 2 and 0 <= ny < w + 2 and visited[nx][ny] == -1:
        if arr[nx][ny] =="." or arr[nx][ny] == "$":
          visited[nx][ny] = visited[a][b]
          q.appendleft([nx,ny])
        elif arr[nx][ny] == "#":
          visited[nx][ny] = visited[a][b] + 1
          q.append([nx,ny])
  return visited
  
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(int(input())):
  h, w = map(int,input().split())
  arr = []
  arr.append(["."] * (w + 2))
  for i in range(h):
    arr.append(["."] + list(input().rstrip()) + ["."])
  arr.append(["."] * (w + 2))
  target = []
  for i in range(1, h + 1):
    for j in range(1, w + 1):
      if arr[i][j] == "$": target.append([i,j])
  visited1 = bfs(0, 0)
  visited2 = bfs(target[0][0], target[0][1])
  visited3 = bfs(target[1][0], target[1][1])    
  ans = int(1e9)
  for i in range(h + 2):
    for j in range(w + 2):
      if visited1[i][j] != -1 and visited2[i][j]!= -1 and visited3[i][j]!= -1:
        cnt = visited1[i][j] + visited2[i][j] + visited3[i][j]
        if arr[i][j] == "*": continue
        if arr[i][j] =="#": cnt -= 2
        ans = min(ans,cnt)
  print(ans)