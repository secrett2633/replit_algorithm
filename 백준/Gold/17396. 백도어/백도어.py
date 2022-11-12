import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = {i : [] for i in range(n)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
q = []
heapq.heappush(q, (0, 0))
visited = [False] * n 
res = int(1e9)
while q:
    cnt, now = heapq.heappop(q)
    if now == n - 1: print(cnt); break
    if visited[now] or arr[now]: continue
    visited[now] = True
    for i, j in graph[now]:
        heapq.heappush(q, (cnt + j, i))
else: print(-1)