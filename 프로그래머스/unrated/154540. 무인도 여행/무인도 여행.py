def solution(maps):
    from collections import deque
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    dx = [0, 0, -1, 1]; dy = [1, -1, 0, 0]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j]:
                q = deque([[i, j]])
                cnt = 0
                while q:
                    x, y = q.popleft()
                    if visited[x][y] or maps[x][y] == "X": continue
                    visited[x][y] = True
                    cnt += int(maps[x][y])
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]): q.append([nx, ny])
                if cnt: answer.append(cnt)        
    return sorted(answer) if answer else [-1]