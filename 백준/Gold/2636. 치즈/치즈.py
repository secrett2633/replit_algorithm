import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = []
def solve():
    q = deque([[0,0]])
    visited[0][0] = 1
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0: visited[nx][ny] = 1; q.append([nx,ny])
                elif graph[nx][ny] == 1: graph[nx][ny] = 0; visited[nx][ny] = 1; cnt += 1
    ans.append(cnt)
    return cnt
res = 0
while True:
    res += 1
    visited = [[0] * m for _ in range(n)]
    if solve() == 0: break
print(res - 1)
print(ans[-2])