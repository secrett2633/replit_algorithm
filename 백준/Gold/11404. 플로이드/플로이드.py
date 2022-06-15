import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[int(1e9)] * (n + 1) for i in range(n + 1)]
for i in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = min(c, graph[a][b])
for i in range(n + 1):
  graph[i][i] = 0
for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if graph[i][k] != int(1e9) and graph[k][j] != int(1e9):
        graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(1, n + 1):
  for j in range(1, n + 1):
    print(graph[i][j] if graph[i][j] != int(1e9) else 0, end = " ")
  print("")