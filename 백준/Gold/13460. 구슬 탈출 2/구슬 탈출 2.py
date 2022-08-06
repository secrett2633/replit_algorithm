import sys
import copy
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
for i in range(n):
  for j in range(m):
    if arr[i][j] == "O": O = [i, j]
    if arr[i][j] == "R": R = [i, j]; arr[i][j] = "."
    if arr[i][j] == "B": B = [i, j]; arr[i][j] = "."
visited = [[[[int(1e9)] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]
q = []
heapq.heappush(q, (1, R[0], R[1], B[0], B[1]))
for _ in range(100):
  #위 아래 왼 오 순으로 진행
  queue = copy.deepcopy(q)
  while queue:
    flag1 = False
    flag2 = False
    cnt, x1, y1, x2, y2 = heapq.heappop(queue)
    sx1, sy1, sx2, sy2 = x1, y1, x2, y2
    if cnt > 10: continue
    x1 -= 1
    while arr[x1][y1] == "." or arr[x1][y1] == "O":
      if arr[x1][y1] == "O": flag1 = True; break
      x1 -= 1
    x1 += 1  
    x2 -= 1
    while arr[x2][y2] == "." or arr[x2][y2] == "O":
      if arr[x2][y2] == "O": flag2 = True; break
      x2 -= 1
    x2 += 1
    if x1 == x2 and y1 == y2: 
      if sx1 > sx2: x1 += 1
      else: x2 += 1
    if flag1 and not flag2: print(cnt); exit(0) 
    if visited[x1][y1][x2][y2] <= cnt or flag2: continue 
    visited[x1][y1][x2][y2] = cnt
    heapq.heappush(q, (cnt + 1, x1, y1, x2, y2))
      
  queue = copy.deepcopy(q)
  while queue:      
    flag1 = False
    flag2 = False
    cnt, x1, y1, x2, y2 = heapq.heappop(queue)   
    sx1, sy1, sx2, sy2 = x1, y1, x2, y2
    if cnt > 10: continue
    x1 += 1
    while arr[x1][y1] == "." or arr[x1][y1] == "O":
      if arr[x1][y1] == "O": flag1 = True; break
      x1 += 1
    x1 -= 1  
    x2 += 1
    while arr[x2][y2] == "." or arr[x2][y2] == "O":
      if arr[x2][y2] == "O": flag2 = True; break
      x2 += 1
    x2 -= 1
    if x1 == x2 and y1 == y2: 
      if sx1 < sx2: x1 -= 1
      else: x2 -= 1
    if flag1 and not flag2: print(cnt); exit(0) 
    if visited[x1][y1][x2][y2] <= cnt or flag2: continue 
    visited[x1][y1][x2][y2] = cnt
    heapq.heappush(q, (cnt + 1, x1, y1, x2, y2))          
  queue = copy.deepcopy(q)
  while queue:
    flag1 = False
    flag2 = False
    cnt, x1, y1, x2, y2 = heapq.heappop(queue)
    sx1, sy1, sx2, sy2 = x1, y1, x2, y2
    if cnt > 10: continue
    y1 -= 1
    while arr[x1][y1] == "." or arr[x1][y1] == "O":
      if arr[x1][y1] == "O": flag1 = True; break
      y1 -= 1
    y1 += 1  
    y2 -= 1
    while arr[x2][y2] == "." or arr[x2][y2] == "O":
      if arr[x2][y2] == "O": flag2 = True; break
      y2 -= 1
    y2 += 1
    if x1 == x2 and y1 == y2: 
      if sy1 < sy2: y2 += 1
      else: y1 += 1
    if flag1 and not flag2: print(cnt); exit(0) 
    if visited[x1][y1][x2][y2] <= cnt or flag2: continue 
    visited[x1][y1][x2][y2] = cnt
    heapq.heappush(q, (cnt + 1, x1, y1, x2, y2))
    
  queue = copy.deepcopy(q)
  while queue:
    flag1 = False
    flag2 = False    
    cnt, x1, y1, x2, y2 = heapq.heappop(queue)
    sx1, sy1, sx2, sy2 = x1, y1, x2, y2
    if cnt > 10: continue
    y1 += 1
    while arr[x1][y1] == "." or arr[x1][y1] == "O":
      if arr[x1][y1] == "O": flag1 = True; break
      y1 += 1
    y1 -= 1  
    y2 += 1
    while arr[x2][y2] == "." or arr[x2][y2] == "O":
      if arr[x2][y2] == "O": flag2 = True; break
      y2 += 1
    y2 -= 1
    if x1 == x2 and y1 == y2: 
      if sy1 < sy2: y1 -= 1
      else: y2 -= 1
    if flag1 and not flag2: print(cnt); exit(0) 
    if visited[x1][y1][x2][y2] <= cnt or flag2: continue           
    visited[x1][y1][x2][y2] = cnt
    heapq.heappush(q, (cnt + 1, x1, y1, x2, y2))    
print(-1)