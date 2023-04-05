from collections import deque
import sys
input = sys.stdin.readline
n, m, k = list(map(int, input().split()))
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
q = deque([[0, 0, 1, 0]])
dx = [0, 0, 1, -1]; dy = [1, -1, 0, 0]
while q:
    x, y, cnt, wall = q.popleft()
    if x == n - 1 and y == m - 1: print(cnt); break
    if visited[wall][x][y]: continue
    visited[wall][x][y] = 1
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and wall + arr[nx][ny] <= k and not visited[wall][nx][ny]:
            q.append([nx, ny, cnt + 1, wall + arr[nx][ny]])
else: print(-1)