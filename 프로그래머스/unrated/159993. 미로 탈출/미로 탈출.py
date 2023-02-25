def solution(maps):
    answer = 0
    from collections import deque
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S": start = [i, j, 0]
            elif maps[i][j] == "E": end = [i, j]
            elif maps[i][j] == "L": b = [i, j]

    q = deque([start])
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    dx = [1, -1, 0, 0]; dy = [0, 0, 1, -1]
    while q:
        x, y, cnt = q.popleft()
        if visited[x][y]: continue
        visited[x][y] = True
        if [x, y] == b: print("!!!!!"); break
        for k in range(4):
            nx = x + dx[k]; ny = y + dy[k]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X":
                q.append([nx, ny, cnt + 1])
    else: return -1
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    q = deque([[x, y, cnt]])
    while q:
        x, y, cnt = q.popleft()
        if visited[x][y]: continue
        visited[x][y] = True
        if [x, y] == end: return cnt
        for k in range(4):
            nx = x + dx[k]; ny = y + dy[k]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X":
                q.append([nx, ny, cnt + 1])
    else: return - 1