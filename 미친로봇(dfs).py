import sys
import math
input = sys.stdin.readline
def dfs(x, y, cnt, p):
    global ans
    if cnt == num:
        ans += p
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if board[nx][ny]:
            continue
        if 0 > nx >= (2 * num) + 1 or 0 > ny >= (2 * num) + 1:
            continue
        board[nx][ny] = 1
        dfs(nx, ny, cnt + 1, p * poss[i] * 0.01)
        board[nx][ny] = 0

num, e, w, n, s = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
poss = [n, e, s, w] 
board = [[0] * (2 * num + 1) for _ in range(2 * num + 1)]
board[num][num] = 1
ans = 0
dfs(num, num, 0, 1)
print(ans)