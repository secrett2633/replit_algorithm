from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
graph = [0] * 100001
visited = [0] * 100001
queue = deque()
queue.append(n)
while queue:
    v = queue.popleft()        
    if v == k:
      print(graph[v])
      arr = []
      temp = v
      for _ in range(graph[v] + 1):
          arr.append(temp)
          temp = visited[temp]
      print(' '.join(map(str, arr[::-1])))
      break
    for i in (v - 1, v + 1, v * 2):
      if 0 <= i <= (100000) and graph[i] == 0:
        queue.append(i)
        graph[i] = graph[v] + 1
        visited[i] = v
      