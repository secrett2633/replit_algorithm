import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = [[0, 0, 0, False]]
visited1 = [[False] * m for _ in range(n)]
visited2 = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    cnt, x, y, w = heapq.heappop(q)
    if w and visited2[x][y]: continue
    if not w and visited1[x][y]: continue
    if w: visited2[x][y] = True
    visited1[x][y] = True
    if cnt > t: continue
    if x == n - 1 and y == m - 1: print(cnt); break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m: 
            if arr[nx][ny] == 0:
                heapq.heappush(q, (cnt + 1, nx, ny, w))
            elif arr[nx][ny] == 2:
                heapq.heappush(q, (cnt + 1, nx, ny, True))
            elif arr[nx][ny] == 1 and w:
                heapq.heappush(q, (cnt + 1, nx, ny, True))
else: print("Fail")
