import sys
from collections import deque
import copy
import math
input = sys.stdin.readline  
R, C = map(int,input().split())
dx = [0, 1, 1, 1, 0, 0, 0, -1, -1 ,-1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
graph  = set()
board = [list(input().strip()) for _ in range(R)]
for i in range(R):
  for j in range(C):
    if board[i][j] == "I": arr = [i,j]
    elif board[i][j] == "R": graph.add((i,j))
for cnt, c in enumerate(input().strip()):  
    c = int(c)
    arr[0] += dx[c]
    arr[1] += dy[c]  
    if (arr[0],arr[1]) in graph: print("kraj", cnt + 1); exit(0)        
    dir = set()
    tmp = set()
    for x, y in graph:
      m = [5, 201]
      for j in range(1,10):
        ax = x + dx[j]
        ay = y + dy[j]
        d = abs(ax - arr[0]) + abs(ay - arr[1])
        if d < m[1]: m = [j, d]
      x += dx[m[0]]
      y += dy[m[0]]
      if [x,y] == arr: print("kraj", cnt + 1); exit(0)
      elif (x,y) in dir: tmp.add((x,y)) 
      else: dir.add((x,y))        
    for x,y in tmp:
      dir.remove((x,y))
    graph = dir 
board = [["." for _ in range(C)] for _ in range(R)]
for x,y in graph:
  board[x][y] = "R"
board[arr[0]][arr[1]] = "I"
for i in range(R):
  print(''.join(board[i]))