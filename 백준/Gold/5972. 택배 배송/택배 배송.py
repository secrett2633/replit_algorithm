import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i : [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
q = []
heapq.heappush(q, (0, 1))
visited = [False] * (n + 1)
while q:
    cnt, now = heapq.heappop(q)
    if visited[now]: continue
    visited[now] = True
    if now == n: print(cnt); break
    for i, j in graph[now]:
        heapq.heappush(q, (cnt + j, i))