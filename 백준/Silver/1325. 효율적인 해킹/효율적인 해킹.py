import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i : [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
res = -1
ans = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    q = deque([i])
    cnt = 0
    while q:
        now = q.popleft()
        if visited[now]: continue
        visited[now] = True
        cnt += 1
        for k in graph[now]:
            q.append(k)
    if res < cnt: res = cnt
    ans.append(cnt)
for i in range(n):
    if ans[i] == res: print(i + 1, end = " ")