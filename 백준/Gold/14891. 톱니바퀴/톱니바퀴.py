import sys
from collections import deque
input = sys.stdin.readline
t = [input().rstrip() for _ in range(4)]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
  cache = [[arr[i][0] - 1, arr[i][1]]]
  for j in range(arr[i][0] - 1, 3):
    if t[j][2] == t[j + 1][6]: break
    else: cache.append([j + 1, cache[-1][1] * -1])
  cache = cache[::-1]
  for j in range(arr[i][0] - 1, 0, -1):
    if t[j][6] == t[j - 1][2]: break
    else: cache.append([j - 1, cache[-1][1] * -1])
  for a, b in cache:
    if b == -1: t[a] = t[a][1:] + t[a][0]
    else: t[a] = t[a][-1] + t[a][:-1]
print((1 if t[0][0] == "1" else 0) + (2 if t[1][0] == "1" else 0) + (4 if t[2][0] == "1" else 0) + (8 if t[3][0] == "1" else 0))