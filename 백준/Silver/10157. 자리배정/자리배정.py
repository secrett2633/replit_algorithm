import sys
input = sys.stdin.readline
c, r = map(int, input().split())
k = int(input())
arr = [[0] * c for i in range(r)]
cnt = 1
dir = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x = r-1
y = 0
if k > r * c:
    print(0)  
else:
  while True:
    if cnt == k:
      print(y + 1, r - x)
      break
    arr[x][y] = cnt
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= r or ny >= c or arr[nx][ny] != 0:
      dir = (dir + 1) % 4
      nx = x + dx[dir]
      ny = y + dy[dir]
    x = nx
    y = ny
    cnt += 1