import sys
from collections import deque
import heapq
input = sys.stdin.readline    
for _ in range(int(input())):  
  n, m = map(int, input().split())
  conn = {i:[] for i in range(1, n + 1)}
  for _ in range(m):
    a, b = map(int, input().split())
    conn[a].append(b)
    conn[b].append(a)
  visited = [False] * (n + 1)
  visited[0] = True
  visited[1] = True
  q = deque([1])
  cnt = 0
  while q:
    x = q.popleft()
    if all(visited): print(cnt); break
    for i in conn[x]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        cnt += 1