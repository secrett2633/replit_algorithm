import sys
from collections import deque
import copy
input = sys.stdin.readline
arr = [list(input().rstrip()) for _ in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
for _ in range(72):
  cache = []
  for i in range(11, -1, -1):
    for j in range(6):
      if arr[i][j] != "." and [i, j] not in cache:
        visited = [[i, j]]
        q = deque([[i, j]])
        while q:
          a, b = q.pop()
          for c in range(4):
            if 0 <= a + dx[c] < 12 and 0 <= b + dy[c] < 6 and arr[a + dx[c]][b + dy[c]] == arr[i][j] and [a + dx[c], b + dy[c]] not in visited:
              visited.append([a + dx[c], b + dy[c]])
              q.append([a + dx[c], b + dy[c]])
        if len(visited) >= 4:          
          for a, b in visited:
            cache.append([a, b])
  if len(cache) > 0: 
    ans += 1
    for a, b in cache:
      arr[a][b] = "."
    tmp = copy.deepcopy(arr)
    arr = [["."] * 6 for _ in range(12)]
    for a in range(6):
      now = 11
      for b in range(11, -1, -1):
        if tmp[b][a] != ".":
          arr[now][a] = tmp[b][a]
          now -= 1
  else: break
print(ans)