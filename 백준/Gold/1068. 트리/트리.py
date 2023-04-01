from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
d = int(input())
graph = {i:[] for i in range(n)}
for i in range(n):
  if arr[i] != -1:
    if i != d: graph[arr[i]].append(i)
  else: start = i
if start == d: print(0)
else:
  cnt = 0
  q = deque([start])
  while q:
    x = q.pop()    
    if graph[x]:
      for i in graph[x]:
        q.append(i)
    else: cnt += 1
  print(cnt)