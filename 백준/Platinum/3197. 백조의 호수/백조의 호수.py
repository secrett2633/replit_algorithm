from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(m)]
visited1 = [[0] * n for _ in range(m)]
visited2 = [[0] * n for _ in range(m)]
target = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q1, q2, temp1, temp2 = deque(), deque(), deque(), deque()

for i in range(m):
  for j in range(n):
    if arr[i][j] == 'L': target.append([i, j]); q2.append([i, j])
    elif arr[i][j] == '.': visited2[i][j] = 1; q2.append([i, j])
for x, y in target:
  arr[x][y] = "."
q1.append([target[0][0], target[0][1]])
visited1[target[0][0]][target[0][1]] = 1
for day in range(1000000):
    while q2:
        x, y = q2.popleft()
        if arr[x][y] == 'X': arr[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited2[nx][ny]:
                    if arr[nx][ny] == 'X': temp2.append([nx, ny])
                    else: q2.append([nx, ny])
                    visited2[nx][ny] = 1
    while q1:
        x, y = q1.popleft()
        if x == target[1][0] and y == target[1][1]: print(day); exit(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited1[nx][ny]:
                    if arr[nx][ny] == '.': q1.append([nx, ny])
                    else: temp1.append([nx, ny])
                    visited1[nx][ny] = 1
    q1, q2 = temp1, temp2
    temp1, temp2 = deque(), deque()