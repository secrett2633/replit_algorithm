import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
comm = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]
nx, ny = x, y
for i in comm:
    if not (0 <= nx + dx[i - 1] < n and 0 <= ny + dy[i - 1] < m): continue
    nx += dx[i-1]
    ny += dy[i-1]
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if i == 1: dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif i == 2: dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif i == 3: dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else: dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
    if board[nx][ny] == 0: board[nx][ny] = dice[-1]
    else: dice[-1] = board[nx][ny]; board[nx][ny] = 0
    print(dice[0])