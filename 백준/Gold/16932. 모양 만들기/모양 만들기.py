import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
unique = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]; dy = [1, -1, 0, 0]
res = 0
un = 1
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            un += 1
            q = deque([[i, j]])
            tmp = []
            while q:
                x, y = q.popleft()
                if visited[x][y]: continue
                visited[x][y] = 1
                tmp.append([x, y])
                for k in range(4):
                    nx = x + dx[k]; ny = y + dy[k]
                    if (0 <= nx < n and 0 <= ny < m) and arr[nx][ny]:
                        q.append([nx, ny])
            for x, y in tmp:
                visited[x][y] = len(tmp)
                unique[x][y] = un
            res = max(res, len(tmp))
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt = 1
            tmp = []
            for k in range(4):
                if (0 <= i + dx[k] < n and 0 <= j + dy[k] < m) and unique[i + dx[k]][j + dy[k]] not in tmp:
                    cnt += visited[i + dx[k]][j + dy[k]]
                    tmp.append(unique[i + dx[k]][j + dy[k]])
            res = max(res, cnt)
print(res)