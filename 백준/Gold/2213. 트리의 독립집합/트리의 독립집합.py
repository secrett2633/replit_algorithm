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
  if not children: return (arr[node], 0, set([node]), set())
  else:
    p, np = arr[node], 0
    p_list, np_list = set([node]), set()
    for child in children:
      cp, cnp, cp_list, cnp_list = dfs(child, visited)
      p += cnp
      for i in cnp_list:
        p_list.add(i)
      if cp >= cnp:
        np += cp        
        for i in cp_list:
          np_list.add(i)
      else:
        np += cnp
        for i in cnp_list:
          np_list.add(i)
        
    return (p, np, p_list, np_list)
a, b, c, d = dfs(1, visited)
if a >= b:
  print(a)
  print(*sorted(list(c)))
else:
  print(b)
  print(*sorted(list(d)))
