import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cache = {1: [[0], [1], [2], [3]],
        2: [[0, 1], [2, 3]],
        3: [[0, 2], [0, 3], [1, 2], [1, 3]],
        4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
        5: [[0, 1, 2, 3]]}

cctv = []
wall = 0
for i in range(n):
  for j in range(m):
    if 1 <= arr[i][j] <= 5: cctv.append([arr[i][j], i, j]) 
    elif arr[i][j] == 6: wall += 1

result = [0]
def dfs(now, graph):
  if now == len(cctv):
    cnt = 0
    for i in range(n):
      for j in range(m):
        if graph[i][j] == "#": cnt += 1
    result[0] = max(result[0], cnt)

  else:
    for i in cache[cctv[now][0]]:
      temp = copy.deepcopy(graph)
      for j in i:
        nx, ny = cctv[now][1] + dx[j], cctv[now][2] + dy[j]
        while 0 <= nx < n and 0 <= ny < m and temp[nx][ny] != 6:
          if temp[nx][ny] == 0: temp[nx][ny] = "#"
          nx, ny = nx + dx[j], ny + dy[j]
      dfs(now + 1, temp)

dfs(0, arr)
print(n * m - result[0] - len(cctv) - wall)