import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
m = 0
for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    if a == 1: graph.append([b, c]); m += 1
    else:
        visited = [False] * m
        q = deque([b - 1])
        while q:
            now = q.popleft()
            if now == c - 1: print(1); break
            visited[now] = True
            for j in range(m):
                if not visited[j] and ((graph[j][0] < graph[now][0] < graph[j][1]) or (graph[j][0] < graph[now][1] < graph[j][1])): q.append(j)
        else: print(0)
            