import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i : [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
for _ in range(m):
    a, b = map(int, input().split())
    q = deque([[0, a]])
    visited = [False] * (n + 1)
    while q:
        cnt, now = q.pop()
        if visited[now]: continue
        visited[now] = True
        if now == b: print(cnt); break
        for i, k in graph[now]:
            q.append([cnt + k, i])