import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0: break
  arr = [list(input().rstrip()) for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if arr[i][j] != "*":
        cnt = 0
        for k in range(8):
          nx, ny = i + dx[k], j + dy[k]
          if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == "*": cnt += 1
        arr[i][j] = cnt
  for i in range(n):
    print("".join(map(str, arr[i])))