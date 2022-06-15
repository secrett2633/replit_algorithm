import sys
import math
input = sys.stdin.readline
a, b = map(int, input().split())
cnt = 0
res = 0
for i in range(1, b + 1):
  for j in range(i):
    cnt += 1
    if cnt > b:
      break
    if a <= cnt:
      res += i
print(res)