import sys
input = sys.stdin.readline
n = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = [[0] * n for _ in range(n)]
graph1 = [[0] * n for _ in range(n)]
for _ in range(n * n):
    now, *arr = map(int, input().split())
    q = [[-1, -1, -1, -1]]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0: continue
            cnt = 0 
            cnt2 = 0
            for x in range(4):
                nx, ny = i + dx[x], j + dy[x]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] in arr: cnt += 1
                    if graph[nx][ny] == 0: cnt2 += 1
            if cnt > q[0][0]: q = [[cnt, cnt2, i, j]]
            elif cnt == q[0][0]: q.append([cnt, cnt2, i, j])
    q.sort(key = lambda x:(x[0], 100 - x[1], x[2], x[3]))
    if q[0][2] != -1 and len(q) == 1: graph[q[0][2]][q[0][3]] = now; graph1[q[0][2]][q[0][3]] = arr
    elif len(q) > 1 and q[0][1] > q[1][1]: graph[q[0][2]][q[0][3]] = now; graph1[q[0][2]][q[0][3]] = arr
    else: graph[q[0][2]][q[0][3]] = now; graph1[q[0][2]][q[0][3]] = arr
res = 0
cache = {0 : 0, 1 : 1, 2: 10, 3 : 100, 4 : 1000}
for i in range(n):
    for j in range(n):
        cnt = 0
        for x in range(4):
            nx, ny = i + dx[x], j + dy[x]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] in graph1[i][j]: cnt += 1
        res += cache[cnt]
print(res)