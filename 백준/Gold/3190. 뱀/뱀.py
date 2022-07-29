import sys
from collections import deque
import copy
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n = int(input())
arr = [["."] * n for _ in range(n)]
arr[0][0] = "S"
k = int(input())
for _ in range(k):
  i, j = map(int, input().split())
  arr[i - 1][j - 1] = "A"
cache = [[False, 0] for _ in range(10001)]
di = {"D" : 1, "L" : 3}
d = 0
for _ in range(int(input())):
  a, b = input().rstrip().split()
  cache[int(a)] = [True, di[b]]
nx = 0
ny = 0
tail = [[0, 0]]
ans = 0
for i in range(10001):
  ans += 1
  if cache[i][0]: d = (d + cache[i][1]) % 4
  nx += dx[d]
  ny += dy[d]
  if 0 > nx or nx >= n or 0 > ny or ny >= n or arr[nx][ny] == "S": break
  if arr[nx][ny] != "A": 
    a, b = tail.pop(0)
    arr[a][b] = "."
  arr[nx][ny] = "S"
  tail.append([nx, ny])
print(ans)