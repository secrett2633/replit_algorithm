from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()        
        if v == k:
          print(graph[v])
          return
        if 0 <= v * 2 and v * 2 <= 100001 and graph[v * 2] == -1:
            graph[v * 2] = graph[v]
            queue.appendleft(v * 2)
        for i in (v - 1, v + 1):
          if 0 <= i and i <= 100001 and graph[i] == -1:
            graph[i] = graph[v] + 1
            queue.append(i)
n, k = map(int, input().split())
graph = [-1] * (100002)
graph[n] = 0
bfs(n)