def solution(board):
    answer = 0
    from collections import deque
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                q = deque([[0, i, j]])
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    dx = [1, -1, 0, 0]; dy = [0, 0, 1, -1]
    while q:
        cnt, x, y = q.popleft()
        if visited[x][y] or board[x][y] == "D": continue
        visited[x][y] = cnt
        if board[x][y] == "G": return cnt
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            while 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != "D":
                nx, ny = nx + dx[k], ny + dy[k]
            q.append([cnt + 1, nx - dx[k], ny - dy[k]])
    return -1