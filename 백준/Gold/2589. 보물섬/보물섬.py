import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            visited = [[False] * m for _ in range(n)]
            q = deque([[i, j, 0]])
            while q:
                a, b, cnt = q.popleft()                
                if visited[a][b]: continue
                res = max(res, cnt)
                visited[a][b] = True               
                for k in range(4):
                    nx, ny = a + dx[k], b + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == "L":
                        q.append([nx, ny, cnt + 1])
print(res)                    