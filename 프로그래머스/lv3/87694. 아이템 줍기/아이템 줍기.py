def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[0] * 104 for _ in range(104)]
    for y1, x1, y2, x2 in rectangle:
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                graph[i][j] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    dx1 = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy1 = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    import heapq
    q = []
    heapq.heappush(q, (0, characterY * 2, characterX * 2))
    visited = [[int(1e9)] * 104 for _ in range(104)]
    while q:
        cnt, x, y = heapq.heappop(q)
        visited[x][y] = cnt
        #if x == itemY and y == itemX: break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (not (0 < nx < 101)) or (not (0 < ny < 101)) or (graph[nx][ny] != 1): continue
            tmp = 0
            #print(nx, ny)
            for j in range(8):
                tmp += graph[nx + dx1[j]][ny + dy1[j]]
            if tmp == 8: continue
            if visited[nx][ny] > cnt + 1: heapq.heappush(q, (cnt + 1, nx, ny))
    
            
                
    return visited[itemY * 2][itemX * 2] // 2
    
    for i in range(21):
        for j in range(21):
            print(" " * (3 - len(str(visited[i][j]))) + str(visited[i][j]), end = " ")
        print()
    
        #상하좌우 확인하고 한칸이라도 비었으면 해당 칸 이동 가능
    for i in range(41):
        for j in range(41):
            if (graph[i][j]): print("O", end = " ")
            else: print("X", end = " ")
        print()
    return answer