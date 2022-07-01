import sys
input = sys.stdin.readline
n = int(input())
tar = int(input())
arr = [[0] * n for _ in range(n)]
x, y = (n - 1) // 2, (n - 1) // 2
arr[x][y] = 1
i = 1
j = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while i < n * n:  
  for k in range(4):
    for _ in range(j):
      x += dx[k]
      y += dy[k]
      i += 1
      arr[x][y] = i
  x -= 1
  y -= 1
  j += 2
for i in range(n):
  print(*arr[i])
  if tar in arr[i]:
    rx, ry = i + 1, arr[i].index(tar) + 1
print(rx, ry)
  