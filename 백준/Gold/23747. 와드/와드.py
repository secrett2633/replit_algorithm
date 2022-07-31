import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline  
s=''
def bfs(I):
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
  queue = deque([I])
  chk[I[0]][I[1]]= '.'
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and chk[nx][ny] == '#' and graph[nx][ny] == s:
        queue.append((nx, ny))
        chk[nx][ny] = '.'
def move(Str,Start):
  global s
  arr=[Start[0] - 1, Start[1] - 1]
  for i in Str:
    if i=='U': arr=[arr[0]-1,arr[1]]
    elif i=='D': arr=[arr[0]+1,arr[1]]
    elif i=='L': arr=[arr[0],arr[1]-1]
    elif i=='R': arr=[arr[0],arr[1]+1]
    elif i=='W': s=graph[arr[0]][arr[1]]; bfs(arr)
  a,b=arr[0],arr[1]
  chk[a][b]='.'
  if a > 0: chk[a - 1][b]='.'
  if a < R - 1: chk[a + 1][b]='.'
  if b < C - 1: chk[a][b + 1]='.'
  if b > 0: chk[a][b - 1]='.'
  return chk
R, C = map(int,input().split())
graph = [list(input()) for _ in range(R)]
chk = [["#"] * C for _ in range(R)]
start = list(map(int,input().split()))
move(input(),start)
for i in chk:
  print("".join(i))