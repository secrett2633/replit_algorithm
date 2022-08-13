import sys
import heapq
input = sys.stdin.readline
n = int(input())
graph = {i:[] for i in range(1, n + 1)}
for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
m = int(input())
q = []
heapq.heappush(q, (0, 1, 1))
visited = [False] * (n + 1)
cache = [int(1e9)] * (n + 1)
parent = [int(1e9)] * (n + 1)
while q:
  cnt, x, px = heapq.heappop(q)
  if visited[x]: continue
  visited[x] = True
  cache[x] = cnt  
  parent[x] = px
  for i in graph[x]:
    heapq.heappush(q, (cnt + 1, i, x))
for _ in range(m):
  a, b = map(int, input().split())
  while cache[a] != cache[b]:
    if cache[a] > cache[b]: a = parent[a]
    else: b = parent[b]
  while a != b:
    a = parent[a]
    b = parent[b]
  print(a)