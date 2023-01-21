import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
graph = {i : [] for i in range(1, 101)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
ans = []
visited = [False] * (n + 1)
q = deque([[t1, 0]])
while q:
    now, cnt = q.popleft()
    if visited[now]: continue
    visited[now] = True
    if now == t2: print(cnt); break
    for k in graph[now]:
        q.append([k, cnt + 1])
else: print(-1)