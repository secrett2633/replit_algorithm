import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def solve(x, y):
    cnt = 0 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                cnt += 1
    return (x, y, cnt) if cnt != 0 else None
def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and arr[nx][ny] != 0:
                dfs(nx, ny)
answer = 0
while True:
    answer += 1
    reduce = deque()  
    for x in range(1, N):
        for y in range(1, M):
            if arr[x][y] != 0:
                h = solve(x, y)
                if h is not None:
                    reduce.append(h)
    while reduce:
        x, y, h = reduce.popleft()
        arr[x][y] = max(arr[x][y] - h, 0)
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    for x in range(1, N):
        for y in range(1, M):
            if arr[x][y] != 0 and not visited[x][y]:
                cnt += 1
                if cnt == 2:
                    break
                dfs(x, y)
    if cnt > 1:
        break
    if sum(map(sum, arr[1:-1])) == 0:
        answer = 0
        break
print(answer)