import sys
import heapq
import copy
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
flag = [[False] * n for _ in range(n)]
location = set()
target = 0
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == "P": start = [i, j]
        elif arr[i][j] == "K": flag[i][j] = True; target += 1
        location.add(graph[i][j])
location = sorted(list(location))
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
res = int(1e20)
left = right = 0
while left < len(location):
    visited = [[False] * n for _ in range(n)]
    q = deque([start[::]])
    cnt = 0
    if location[left] <= graph[start[0]][start[1]] <= location[right]:
        while q:
            x, y = q.popleft()
            if visited[x][y]: continue
            visited[x][y] = True
            if flag[x][y]: cnt += 1
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if (0 <= nx < n and 0 <= ny < n) and (location[left] <= graph[nx][ny] <= location[right]):
                    q.append([nx, ny])
    if cnt == target: res = min(res, location[right] - location[left]); left += 1
    elif right + 1 < len(location): right += 1
    else: break
print(res)