import sys
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [True] * 26
def solve(x, y, now):
  global result
  result = max(now, result)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c and visited[ord(arr[nx][ny]) - 65]:
      visited[ord(arr[nx][ny]) - 65] = False
      solve(nx, ny, now + 1)
      visited[ord(arr[nx][ny]) - 65] = True
visited[ord(arr[0][0]) - 65] = False
solve(0, 0, 1)
print(result)