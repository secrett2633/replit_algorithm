import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0: break
    graph = []
    for i in range(l):
        graph.append([list(input().rstrip()) for _ in range(r)])
        input()
    q = deque()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == "S": q.append([0, i, j, k])
                elif graph[i][j][k] == "E": target = [i, j, k]
    while q:
        cnt, i, j, k = q.popleft()
        if [i, j, k] == target: print(f"Escaped in {cnt} minute(s)."); break
        if graph[i][j][k] == "#": continue
        graph[i][j][k] = "#"
        for z in range(6):
            nx, ny, nz = i + dx[z], j + dy[z], k + dz[z]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                q.append([cnt + 1, nx, ny, nz])
    else: print("Trapped!")