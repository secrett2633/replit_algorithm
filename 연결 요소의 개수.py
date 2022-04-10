from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [False] * (n + 1)
cnt = 0
for i in range(1, n + 1):
  if not visited[i]:    
    cnt += 1
    bfs(i)
print(cnt)