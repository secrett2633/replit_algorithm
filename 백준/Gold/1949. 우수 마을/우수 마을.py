import sys
sys.setrecursionlimit(10 ** 8)
from collections import deque
import heapq
input = sys.stdin.readline    
n = int(input())
arr = [0] + list(map(int, input().split()))
graph = {i : [] for i in range(1, n + 1)}
for i in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [False] * (n + 1)
def dfs(node, visited):
  visited[node] = True
  children = [i for i in graph[node] if not visited[i]]
  if not children: return (arr[node], 0)
  else:
    p, np = arr[node], 0
    for child in children:
      cp, cnp = dfs(child, visited)
      p += cnp
      np += max(cp, cnp)
    return (p, np)
print(max(dfs(1, visited)))
  