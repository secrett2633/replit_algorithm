import sys
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
  n, m, k = map(int,input().split())    
  graph = {i:[] for i in range(1, n + 1)}
  for i in range(k):
    a, b, c, d = map(int,input().split())
    graph[a].append([b, c, d])
  visited = [[int(1e9)] * (n + 1) for _ in range(m + 1)]
  q = [[0,0,1]]
  while q:
    cost, time, now = heapq.heappop(q)
    if cost > visited[time][now]: continue
    for v, c, d in graph[now]:
      if time + c <= m and cost + d < visited[time + c][v]:
        for i in range(time + c,m+1):
          if visited[i][v] > cost + d: visited[i][v] = cost + d
          else: break
        heapq.heappush(q,(cost + d,time + c,v))
  print(visited[m][n] if visited[m][n] != int(1e9) else "Poor KCM")