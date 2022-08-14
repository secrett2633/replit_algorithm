import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque
import heapq
input = sys.stdin.readline    
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
def dfs(now, visited):
  visited[now] = True
  children = [i for i in graph[now] if not visited[i]]
  p, np = 1, 0
  if not children: return (p, np)
  else:
    for child in children:
      cp, cnp = dfs(child, visited)
      p += min(cp, cnp)
      np += cp
    return (p, np)
visited = [False for _ in range(n + 1)]
print(min(dfs(1, visited)))
    