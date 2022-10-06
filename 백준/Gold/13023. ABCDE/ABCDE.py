import sys
import heapq
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i : [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
q = deque([[1, i, [i]] for i in range(n)])
while q:
    cnt, now, visited = q.pop()
    if cnt == 5: print(1); break
    for i in graph[now]:
        if i not in visited:
            q.append([cnt + 1, i, visited + [now]])
else: print(0)