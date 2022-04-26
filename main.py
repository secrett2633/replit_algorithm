import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [int(1e9)] * (n + 1)
visited = [-1] * (n + 1)
for i in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  
tx, ty = map(int, input().split())

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
        visited[i[0]] = now

dijkstra(tx) 
print(distance[ty])

result = [ty]
temp = ty
while visited[temp] != -1:
    result.append(visited[temp])
    temp = visited[temp]
print(len(result))
for i in result[::-1]:
  print(i, end=' ')
print("")