import sys
from collections import deque
import copy
input = sys.stdin.readline
def rotate_2d(list_2d):
  n = len(list_2d)
  m = len(list_2d[0])
  new = [[0] * n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      new[j][n-i-1] = list_2d[i][j]
  return new
def can_put(a, b, r, c):
  for i in range(r):
    for j in range(c):
      if sticker[i][j] == 1 and arr[i + a][j + b] == 1: return False
  return True       
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for _ in range(k):
  r, c = map(int, input().split())
  sticker = [list(map(int, input().split())) for _ in range(r)]
  flag = True
  for t in range(4):
    r = len(sticker)
    c = len(sticker[0])
    for a in range(n - r + 1):
      for b in range(m - c + 1):
        if not flag: break
        if can_put(a, b, r, c):
          flag = False
          for i in range(r):
            for j in range(c):
              if sticker[i][j] == 1: arr[i + a][j + b] = 1
    sticker = rotate_2d(sticker)
ans = 0
for i in range(n):
  ans += sum(arr[i])
print(ans)