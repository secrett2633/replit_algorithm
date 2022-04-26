import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
v1, v2 = map(int, input().split())
result = [0, 0]
distance = [INF] * (n + 1)
dijkstra(1)
result[0] += distance[v1]
result[1] += distance[v2]
distance = [INF] * (n + 1)
dijkstra(v1)
result[0] += distance[v2]
result[1] += distance[n]
distance = [INF] * (n + 1)
dijkstra(v2)
result[1] += distance[v1]
result[0] += distance[n]
print(min(result[0], result[1]) if min(result[0], result[1]) < INF else "-1")