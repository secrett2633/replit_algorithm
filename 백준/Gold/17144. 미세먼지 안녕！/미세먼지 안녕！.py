import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
cleaner = []
board = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
  if board[i][0] == -1:
    cleaner.append((i, 0))

for _ in range(t):
    steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not (board[i][j] == 0 or board[i][j] == -1):
                turn = 0
                for dx, dy in steps:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in cleaner:
                        turn += 1
                        temp[nx][ny] += board[i][j] // 5
                board[i][j] = board[i][j] - (board[i][j] // 5 * turn)
    for i in range(r):
        for j in range(c):
            board[i][j] += temp[i][j]

    up_step = [[0, 1], [-1, -0], [0, -1], [1, 0]]
    direct = 0
    x, y = cleaner[0]
    up, y = x, 1
    previous = 0
    while True:
        nx, ny = x + up_step[direct][0], y + up_step[direct][1]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        board[x][y], previous = previous, board[x][y]
        x, y = nx, ny
      
    down_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direct = 0
    x, y = cleaner[1]
    down, y = x, 1
    previous = 0
    while True:
        nx, ny = x + down_step[direct][0], y + down_step[direct][1]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        board[x][y], previous = previous, board[x][y]
        x, y = nx, ny

result = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            result += board[i][j]

print(result)