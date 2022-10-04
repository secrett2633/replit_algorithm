import sys
import heapq
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sec, x, y = map(int, input().split())
q = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            for s in range(4):
                nx, ny = i + dx[s], j + dy[s]
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                    heapq.heappush(q, (arr[i][j], nx, ny))

for d in range(sec):
    aq = []
    while q:
        now, a, b = heapq.heappop(q)
        if arr[a][b] != 0: continue
        arr[a][b] = now
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                heapq.heappush(aq, (now, nx, ny))
    q = aq
print(arr[x - 1][y - 1])