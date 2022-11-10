import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
visited = [[False] * m for _ in range(n)] 
res = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cache = []
            q = deque([[i, j]])
            visit = [[False] * m for _ in range(n)]
            while q:
                x, y = q.popleft()
                if visit[x][y]: continue
                visit[x][y] = True
                cache.append([x, y])
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == arr[i][j]:
                        q.append([nx, ny])
            flag = True
            for x, y in cache: 
                visited[x][y] = True
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] > arr[i][j]: flag = False
            if flag: 
                res += 1
                        
print(res)