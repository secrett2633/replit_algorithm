N, M, R = map(int, input().split())
graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]
item = list(map(int, input().split()))
item.insert(0, 0)
for _ in range(R):
  a, b, c = map(int, input().split())
  graph[a][b] = min(c, graph[a][b])
  graph[b][a] = min(c, graph[b][a])
for k in range(1, N + 1): 
    for i in range(1, N + 1):
        for j in range(1, N + 1): 
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
            if i == j:
              graph[i][j] = 0
result = 0
for i in range(1, N + 1):
  temp = 0
  for j in range(1, N + 1):
    if graph[i][j] <= M:
      temp += item[j]
  result = max(temp, result)
print(result)