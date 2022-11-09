import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if arr1[i][j] != arr2[i][j]:
            q = deque()
            q.append([i, j])
            visited = [[False] * m for _ in range(n)]
            cache = []
            while q:
                x, y = q.popleft()
                if visited[x][y]: continue
                visited[x][y] = True
                cache.append([x, y])
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr1[nx][ny] == arr1[i][j]:
                        q.append([nx, ny])
            for x, y in cache:
                arr1[x][y] = arr2[i][j]
            if arr1 == arr2: print("YES")
            else: print("NO")
            exit(0)
print("YES")
