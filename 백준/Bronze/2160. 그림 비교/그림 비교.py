import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
n = int(input())
res = int(1e9)
ans = [0, 0]
arr = [[list(input().rstrip()) for _ in range(5)] for _ in range(n)]
for i in range(n - 1):
  for j in range(i + 1, n):
    cnt = 0
    for a in range(5):
      for b in range(7):
        if arr[i][a][b] != arr[j][a][b]: cnt += 1
    if res > cnt: res = cnt; ans = [i + 1, j + 1]
print(*ans)