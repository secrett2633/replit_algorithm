import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** n)]
query = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(q):
  for j in range((2 ** n) // (2 ** query[i])):
    for k in range((2 ** n) // (2 ** query[i])):
      tmp = [[0] * (2 ** query[i]) for _ in range(2 ** query[i])]
      for a in range(2 ** query[i]):
        for b in range(2 ** query[i]):
          tmp[b][2 ** query[i] - a - 1] = arr[a + (2 ** query[i]) * j][b + (2 ** query[i]) * k]
      for a in range(2 ** query[i]):
        for b in range(2 ** query[i]):
          arr[a + (2 ** query[i]) * j][b + (2 ** query[i]) * k] = tmp[a][b]
  cache = deque([])
  for a in range(2 ** n):
    for b in range(2 ** n):
      cnt = 0
      for c in range(4):
        if 0 <= a + dx[c] < 2 ** n and 0 <= b + dy[c] < 2 ** n and arr[a + dx[c]][b + dy[c]] > 0: cnt += 1
      if cnt < 3: cache.append([a, b])        
  while cache:
    a, b = cache.pop()
    arr[a][b] = max(arr[a][b] - 1, 0)
res = 0
ans = 0
for i in range(2 ** n):
  for j in range(2 ** n): 
    ans += max(arr[i][j], 0)
for i in range(2 ** n):
  for j in range(2 ** n):    
    if arr[i][j] == 0: continue
    q = deque([[i, j]])
    cnt = 1
    arr[i][j] = 0
    while q:
      i, j = q.pop()
      for c in range(4):
        if 0 <= i + dx[c] < 2 ** n and 0 <= j + dy[c] < 2 ** n and arr[i + dx[c]][j + dy[c]] > 0:
          cnt += 1
          arr[i + dx[c]][j + dy[c]] = 0
          q.append([i + dx[c], j + dy[c]])
    res = max(res, cnt)
print(ans)
print(res)