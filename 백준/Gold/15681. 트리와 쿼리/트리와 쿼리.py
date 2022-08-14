import sys
sys.setrecursionlimit(10 ** 8)
from collections import deque
import heapq
input = sys.stdin.readline    
n, r, q = map(int, input().split())
graph = {i : [] for i in range(1, n + 1)}
for i in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
res = [0] * (n + 1)
visited = [False] * (n + 1)
def dfs(node, visited):
  visited[node] = True
  children = [i for i in graph[node] if not visited[i]]
  if not children: res[node] = 1; return 1
  else:
    cnt = 1
    for child in children:
      cnt += dfs(child, visited)
    res[node] = cnt
    return cnt
dfs(r, visited)
for _ in range(q):
  u = int(input())
  print(res[u])